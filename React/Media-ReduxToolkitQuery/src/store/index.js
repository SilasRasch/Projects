import { configureStore, getDefaultMiddleware } from '@reduxjs/toolkit';
import { setupListeners } from '@reduxjs/toolkit/dist/query';
import { usersReducer } from './slices/usersSlice';
import { albumsApi } from './apis/albumsApi';
import { photosApi } from './apis/photosApi';

export const store = configureStore({
  reducer: {
    users: usersReducer,
  //albums: albumsApi.reducer         - dette ville også virke 
    [albumsApi.reducerPath]: albumsApi.reducer, //dette er en mere sikker måde, ungår "typo's"
    [photosApi.reducerPath]: photosApi.reducer
  },
  middleware: (getDefaultMiddleware) => {
    return getDefaultMiddleware()
    .concat(albumsApi.middleware)
    .concat(photosApi.middleware);
  }
});

setupListeners(store.dispatch);


export * from './thunks/fetchUsers';
export * from './thunks/addUser';
export * from './thunks/removeUser';
export { useFetchAlbumsQuery, useAddAlbumMutation, useRemoveAlbumMutation } from './apis/albumsApi';
export { useFetchPhotosQuery, useAddPhotoMutation, useRemovePhotoMutation } from './apis/photosApi';
