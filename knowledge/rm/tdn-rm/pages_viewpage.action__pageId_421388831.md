---
content_hash: cc819a8491d506938857eca872664ec2a4b883b7189681f4d37e86b4f653365d
fetched_at: '2026-06-29T00:09:19.219576+00:00'
page_id: '421388831'
product: rm
source: tdn-rm
title: Copia entre Coligadas - Cliente / Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388831
version: 7
---

O objetivo deste processo é realizar a cópia de informações de um registro de uma coligada para outra coligada. Se você precisar incluir registros em uma coligada, que sejam idênticos a registros de outra coligada, não faça manualmente, utilize o processo de "Cópia entre Coligadas". A tarefa será realizada com mais agilidade e com mais segurança.

Marque os registros a serem copiados, acesse o "processo" "Cópia entre Coligadas", marque a coligada para onde as informações serão copiadas e confirme a operação.

Se a opção **Substitui registros no destino se eles já existirem**for selecionada, o processo atualizará os dados do cliente/fornecedor e substituirá as informações das tabelas dependentes com as informações da coligada de origem.

**Observações**

Não é possível realizar a cópia de determinado campo se na coligada de destino não existir o valor correspondente para tal campo. Quando este fato ocorrer você tem duas opções para realizar a cópia:

1. Excluir o valor do campo, salvar a edição e repetir o processo;
2. Acessar a outra coligada, criar o registro para o campo e repetir o processo.

Se ocorrer algum problema na cópia de alguma informação do registro de cliente/fornecedor, nenhuma outra informação ou anexo serão copiados.

Se ocorrer problema na cópia das informações de algum dos cadastros de anexos e campos complementares, nenhum deles será salvo para o registro em questão. As informações do registro de cliente/fornecedor serão copiadas.

Se na coligada de destino estiver definido que alguma informação do cadastro de anexo é obrigatória e na coligada de origem não existir esta informação, nenhuma outra informação do registro de anexo será copiada.

Clientes/Fornecedores "Globais" não podem ser copiados entre Coligadas.

Se na coligada de destino o parâmetro "Permite nomes iguais para contatos para o mesmo Cli/For" (Assistente de Implantação de Processos | etapa Parâmetros Gerais do Cliente/Fornecedor) estiver desmarcado e na coligada de origem existir contatos com nomes iguais, apenas as informações de um dos contatos serão copiadas.

O código do cliente/fornecedor não é alterado na cópia entre coligadas.
