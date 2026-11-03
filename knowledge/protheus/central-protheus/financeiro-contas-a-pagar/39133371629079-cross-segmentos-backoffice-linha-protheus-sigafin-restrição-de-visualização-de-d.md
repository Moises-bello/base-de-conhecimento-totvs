---
article_id: 39133371629079
category: Financeiro - Contas a Pagar
content_hash: e13881b80384b010f274a1ea8c21c764239b6786e49daa33b710fe3c9c994601
fetched_at: '2026-06-28T22:38:09.809373+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Restrição de visualização
  de dados sensíveis e pessoais - LGPD
type: support-article
updated_at: '2026-03-23T22:09:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39133371629079-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Restri%C3%A7%C3%A3o-de-visualiza%C3%A7%C3%A3o-de-dados-sens%C3%ADveis-e-pessoais-LGPD
---

**Dúvida**  
Por que ao acessar a rotina algumas rotinas, como exemplo Funções Contas a Pagar (FINA050), alguns dados como nome do fornecedor, dados bancários e aprovador são exibidos com asteriscos (\*\*\*), impedindo a visualização das informações pelo usuário?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.2310  
  
**Solução**

O comportamento ocorre devido à configuração de **Controle de Dados Sensíveis e Pessoais** vinculada ao perfil do usuário. Quando as permissões de acesso a esses dados não estão ativas, o sistema mascara as informações em telas, emissões e relatórios para garantir a conformidade com políticas de segurança de dados (LGPD).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39133371623703)

A gestão dessas permissões é realizada pelo **Administrador do Sistema** através do módulo **Configurador (SIGACFG)**.

Para regularizar a visualização, siga o procedimento abaixo:

1. Acesse o módulo **Configurador (SIGACFG)**;
2. Vá em **Usuário/Senhas -> Usuários**;
3. Selecione o usuário que apresenta a restrição e clique em **Alterar**;
4. Acesse a aba **Restrições de Acesso -> Acessos**;
5. Localize e habilite os seguintes itens de segurança:

   * **192 – Acesso a dados sensíveis**
   * **193 – Acesso a dados pessoais**  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39133371623831)
6. Clique em **Confirmar** para salvar as alterações;
7. Solicite ao usuário que realize um novo login no sistema para que as permissões sejam atualizadas.

> **Observação:** Essa configuração também pode ser aplicada a um **Grupo de Usuários**, caso a restrição atinja múltiplos perfis simultaneamente.  
>   
> É importante validar a regra do grupo, pois ela pode ter prioridade ou ser desconsiderada ao realizar a marcação (flag) do controle.
