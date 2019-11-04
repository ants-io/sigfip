jQuery(function($) {
  'use strict';

  var Util = {
    get: async function(url) {
      result = await fetch(url);
    }
  };

  var App = {
    init: function() {
      this.bindEvents();
    },

    bindEvents: function() {
      $('#id_category').on('change', this.updateTitle.bind(this));
      $('#id_category').on('change', this.fetchDocuments.bind(this));
    },

    updateTitle: event => {
      let title = $('#id_category option:selected').text();
      if (title.includes('--')) {
        title = 'Demande de prêt';
      }
      $('#category_title_id').html(title);
    },

    fetchDocuments: event => {
      const loanCategoryId = event.currentTarget.value;

      fetch(`/api/v1/loan_categories/${loanCategoryId}/documents.json`)
        .then(response => response.json())
        .then(data => {
          data.forEach(spec => {
            const row = `
              <tr>
                <td>
                  ${spec.name}
                  <input type="hidden" name="document_id" value="${spec.id}"/>
                </td>
                <td>${spec.required_number}</td>
                <td><input type="text" name="provided_number" class="filter__group__textarea"/></td>
                <td><input type="text" name="reference" class="filter__group__textarea"/></td>
                <td><input type="text" name="document_date" class="filter__group__textarea"/></td>
              </tr>
            `;
            $('#loan_table_id tr:last').after(row);
          });
        });
    }
  };

  App.init();
});
