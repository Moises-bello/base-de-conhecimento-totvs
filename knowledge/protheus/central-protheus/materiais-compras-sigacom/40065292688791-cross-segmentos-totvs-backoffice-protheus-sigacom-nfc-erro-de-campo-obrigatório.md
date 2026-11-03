---
article_id: 40065292688791
category: Materiais - Compras (SIGACOM)
content_hash: 6ec15bdbffcba8dcaa07c8a150806550cb0d2ba4808eeb1c643f1100597ed4de
fetched_at: '2026-06-28T22:41:21.778654+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Erro de "Campo
  Obrigatório" ao adicionar ou editar Contato do Fornecedor
type: support-article
updated_at: '2026-04-28T11:34:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40065292688791-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Erro-de-Campo-Obrigat%C3%B3rio-ao-adicionar-ou-editar-Contato-do-Fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40065249729943) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Durante a geração da cotação no Novo Fluxo de Compras, ao tentar **adicionar ou editar um contato de um fornecedor**, o sistema exibe um alerta indicando a **falta de preenchimento de campos obrigatórios**.

"Não é possível completar a ação. Existem campos obrigatórios não preenchidos"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40065292680599)

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Compras/GCT - A partir da Release 12.1.2310  
  
**Causa**  
A validação que impede a conclusão do processo não é originada do formulário de contatos de fornecedor **DKI (Contatos x Fornecedores)**, mas sim do cadastro principal do fornecedor **SA2**.

Portanto, existem **campos obrigatórios não preenchidos na tabela SA2** (tabela referente ao Cadastro de Fornecedor). Ao processar a adição ou edição do contato na cotação, o sistema realiza uma checagem de integridade do fornecedor e dispara o *help* devido à ausência desses dados obrigatórios na SA2.  
  
**Solução**  
Para solucionar o problema reportado, basta efetuar o procedimento abaixo.

1. **Acesse a rotina padrão de Cadastro de Fornecedores** no sistema.
2. **Localize o cadastro do fornecedor** exato em que a tentativa de edição/inclusão de contato apresentou o erro.
3. Clique na opção **Alterar** (ou Editar) para abrir o formulário principal do fornecedor e clique em Salvar
4. O sistema irá acusar qual ou quais **campos obrigatórios estão em branco** (geralmente destacados ou sinalizados ao tentar confirmar a tela).
5. **Preencha as informações faltantes** e confirme a gravação (salve) do cadastro do fornecedor.
6. Após a validação e correção do fornecedor, **retorne à rotina de Cotação no Novo Fluxo de Compras** e refaça a operação de incluir/editar o contato.

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)
