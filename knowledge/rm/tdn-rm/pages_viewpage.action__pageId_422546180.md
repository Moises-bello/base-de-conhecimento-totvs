---
content_hash: 8cc294d02affd045d327ad776e3972610e34b4d173c019da600decf6f4a28c54
fetched_at: '2026-06-29T00:09:23.972380+00:00'
page_id: '422546180'
product: rm
source: tdn-rm
title: Informações Específicas nos Tipos de Movimento (NFS-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546180
version: 3
---

Algumas informações devem ser gravadas nos tipos de movimento utilizados para a emissão da NFS-e. Algumas destas informações variam de acordo com a prefeitura e geralmente são encontradas no manual de integração da NFS-e fornecido pela prefeitura.

**Mov - Identificação** : Série - Verificar no manual de integração da prefeitura se deve ser enviada alguma série específica.

**Mov - Outros Dados**: Usar Cópia de Movimentos por Referência. Gravar neste campo o valor 19-Substituição NFe - Serviço quando o processo de substituição for executado para uma filial de Belo Horizonte.

**Mov - Edita Movimento Relacionado**: Marque esta opção quando processo de substituição for executado para uma filial que não seja de Belo Horizonte.  Preencha o campo Nome Mov. Relacionado com a expressão :"NFS-e Substituída".

**Item - Identificação 1/2**: Tipo do Itens - Grave o valor Serviços.

**Fin - Condições de Pagamento**: Edita Condição de Pagamento - Utilize este parâmetro se a prefeitura solicita informações a respeito da fatura da NFS-e.

**Fin - Condições de Pagamento**: Condição de Pagamento Default - Utilize esta opção se a prefeitura solicita informações a respeito da fatura da NFS-e e caso queira deixar um valor padrão para sempre que uma nota for emitida.

**Fis - Natureza**: Edição - Deve ser gravado como Edita ou Mostra pois a  é obrigatória para movimentos que irão gerar NFS-e.

**Fis - Natureza**: Seleção Automática da Natureza: Obrigatoriamente deve-se gravar o valor Seleciona por Item para movimentos que irão gerar NFS-e.

**Fis - Dados**: Editar Município por Item - Este parâmetro deve ser gravado como Edita para movimentos que irão gerar NFS-e.

**Fis - Escrituração**: Gerar Escrituração - Marque esta opção para que os movimentos gerados com este tipo possa ser escriturado e os tributos gerados pelas NFS-e possa ser apurados pelo TOTVS Gestão Fiscal.

**Fis - Escrituração**: Tipo de Documento Escrituração - Código Default : Preencha este campo com o [Código do Modelo de Documento](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388695) que será gerado na escrituração da NFS-e.

**Fis - Tributação Item**: Utilizar Tributação dos Itens - Para a NFS-e o Tributo ISSQN obrigatoriamente deve ser gravado no item do movimento.

**Fis - Tributação Movimento**: Utilizar Tributação dos Movimentos - Devem ser gravados no movimento as Retenções IRRF e INSS quando os mesmos incidirem na NFS-e.

**Fis - NF-e**: NFS-e Muncipal (Modelo Nacional) - Se gravado Não integrado este tipo de movimento não irá gerar NFS-e.  Se gravado Envia NFS-e Manualmente este tipo de movimento irá gerar NFS-e e a mesma será enviada manualmente para a prefeitura. Se gravado Envia NFS-e Automaticamente este tipo de movimento irá gerar NFS-e e quando o movimento for salvo a NFS-e será automaticamente enviada para a Prefeitura.
