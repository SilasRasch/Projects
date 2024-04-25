import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { faker } from '@faker-js/faker';


// DEV ONLY!!!
const pause = (duration) => {
    return new Promise((resolve) => {
      setTimeout(resolve, duration);
    });
  };

const albumsApi = createApi({
    reducerPath: 'albums',       //specificere hvor alt state skal gemmes i Store, 'albums' string der angiver "key" i storen
    baseQuery: fetchBaseQuery({  //funktion der returnere et prækonfigureret version af 'fetch'
        baseUrl: 'http://localhost:3005',  //adressen på json-server, der kører på port 3005 
        fetchFn: async (...args) => {await pause(1000); return fetch(...args);} //DEV ONLY - så vi kan se spinner i aktion
    }),
    endpoints(builder){
        return {
            addAlbum: builder.mutation({
              //invalidatesTags: ['Album'],   //benytter Tags, når mutation kaldes sættes Tag til invalid og der laves et nyt fetch
              //invalidatesTags: (result, error, user) => { return [{type: 'Album', id: user.id}];},  //dynamiske Tags
                invalidatesTags: (result, error, user) => { return [{type: 'UsersAlbums', id: user.id}];},
                query: (user) =>{
                    return {
                        url: '/albums', 
                        method: 'POST',
                        body: {
                            userId: user.id,
                            title: faker.commerce.productName()
                        }
                    };
                }
            }),
            removeAlbum: builder.mutation({
                //invalidatesTags: ['Album'],   //benytter Tags, når mutation kaldes sættes Tag til invalid og der laves et nyt fetch
                //invalidatesTags: (result, error, album) => { return [{type: 'Album', id: album.userId}];},  //dynamiske Tags
                  invalidatesTags: (result, error, album) => { return [{type: 'Album', id: album.id}];},
                  query: (album) => {
                      return {
                          url: `albums/${album.id}`, 
                          method: 'DELETE'
                      };
                  }
              }),
            fetchAlbums: builder.query({
             // providesTags: ['Album'],  kunne benyttes, men resultere i at alle users album bliver requestet igen
            //  providesTags: (result, error, user) => { return [{type: 'Album', id: user.id}];}, //dynamisk generering af Tag
                
            providesTags: (result, error, user) => {  //her tages højde for både add og remove
                    const tags = result.map(album => { return {type: 'Album', id: album.id} }); 
                    tags.push({type: 'UsersAlbums', id: user.id});
                    return tags;
                },

                query: (user) =>{
                    return {
                        url: '/albums', 
                        params: {userId: user.id},
                        method: 'GET'
                    };
                }
            })
        }
    }
});

export const { useFetchAlbumsQuery, useAddAlbumMutation, useRemoveAlbumMutation } = albumsApi;
export { albumsApi };