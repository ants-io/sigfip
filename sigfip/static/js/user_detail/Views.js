import hh from 'hyperscript-helpers';
import { h } from 'virtual-dom';

const { div, h3 } = hh(h);

function view(dispatch, model) {
  return div({ className: 'wrapper' }, [
    div({ className: 'banner' }, [h3({ className: 'p-15' }, '_title_')])
  ]);
}

export default view;
