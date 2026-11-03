---
content_hash: 1ee74d44515140b39885139205e2f3a357afa7039f3091547f46db9bb5d9daf3
fetched_at: '2026-06-29T00:05:53.039263+00:00'
page_id: '1064374005'
product: rm
source: tdn-rm
title: Propostas - Documentos da Pessoa
type: documentation
url: https://tdn.totvs.com/display/LRM/Propostas+-+Documentos+da+Pessoa
version: 2
---

## **Como configurar:**

---

Primeiramente, será necessário configurar os tipos de documentos que deverão ser incluídos no cadastro da Pessoa. Esses documentos são essenciais para a validação de dados necessários para a aquisição ou locação de um imóvel, como: documentos de identificação, comprovantes de endereço, documentos financeiros, entre outros.

Para realizar essa configuração, acesse: **Backend > Globais > Documentos da Proposta**. Na tela, clique em "Adicionar" e preencha os campos:

* **Título**: Informe o nome dos documentos que serão solicitados no cadastro da Pessoa (ex.: Comprovante de Residência Atualizado, Cópia da CNH).
* **Tipo de Pessoa**: Indica o tipo de pessoa que deverá apresentar essas informações no cadastro.
* **Vinculado a**: Defina se a documentação estará vinculada à Proposta ou à Pessoa.
* **Tipo**: Defina a quem a solicitação de documentos se aplica (ex.: Prospect, Procurador, Procurador do Cônjuge, Fiador).
* **Estado Civil**: Especifica para qual estado civil informado no cadastro da Pessoa a documentação será solicitada.

Opções:

* **Obrigatório**: Indica se a documentação é obrigatória.
* **Ativo**: Define se a opção está ativa.
* **Exigir Upload**: Indica se é necessário o envio do documento.
* **Instruções de Envio e Instruções de Verificação**: Campos onde podem ser fornecidas instruções específicas sobre o envio e verificação do documento.

## **Na visão de Propostas:**

---

Ao acessar a tela Proposta , no menu **Documentos da Pessoa**, será possível incluir documentos com base no registro de cada documentação solicitada na visão.

Além disso, nesta tela, o corretor pode realizar algumas ações relacionadas aos documentos. As opções disponíveis são:

* **Excluir**: Exclui o documento.
* **Aprovar**: Permite ao corretor aprovar o documento inserido.
* **Reprovar**: Permite ao corretor reprovar o documento inserido.
* **Escolher**: Inclui o documento no cadastro de documentos. É **preferível** que o nome/descrição do arquivo para upload seja informado **sem espaços**.
* **Download de Documentos:** Após a aprovação ou a conclusão do processo de análise, os usuários têm a facilidade de baixar os documentos relacionados à pessoa. Isso é especialmente útil para manter registros precisos e acessíveis.

**Importante:**

* O limite de upload de documentos a partir da versão 12.1.32 passa a ser de 10mb por arquivo.
* A função **'Baixar Todos**' só pode ser utilizada com documentos já gravados no sistema. Portanto, ao inserir novos arquivos, é necessário salvá-los antes de acionar este botão.

A inclusão de documentos, a capacidade de aprovar ou reprovar e a facilidade de download tornam o sistema uma ferramenta completa para otimizar o gerenciamento de propostas.

**Concorrência de usuários ao editar ou baixar documentos**

Realizamos melhorias no controle do upload e edição de documentos no Portal de Imóveis, especialmente quando essas atividades ocorrem ao mesmo tempo por vários usuários.

Nesse cenário, o Portal de Imóveis priorizará o usuário que iniciou a edição dos documentos primeiro. Dessa forma, os usuários subsequentes terão acesso à tela de documentos da pessoa apenas para leitura, aguardando a conclusão do processo de upload ou edição pelo usuário inicial e o fechamento correspondente da tela.

Essa abordagem foi implementada para evitar o envio simultâneo de documentos duplicados, o que poderia causar inconsistências no sistema. Com esse controle mais preciso, buscamos assegurar uma experiência eficiente e livre de duplicidades no gerenciamento de documentos no Portal de Imóveis.
