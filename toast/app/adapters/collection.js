import JamAdapter from 'toast/mixins/jam-adapter';

export default JamAdapter.extend({
    createRecordUrlTemplate: '{+host}/v2/namespaces{/namespaceId}/collections',

    urlSegments: {
      namespaceId(type, id, snapshot) {
        return snapshot.record.get('namespace.id');
      }
    }
});
