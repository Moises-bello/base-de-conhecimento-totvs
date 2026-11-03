---
article_id: 35816163879191
category: eConsignado (Crédito do Trabalhador)
content_hash: 7956e5d7e38db6ab87e236e1d5ad4954181b0727b2c320e058858971c09e545f
fetched_at: '2026-06-28T22:43:07.305210+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Importação Crédito do Trabalhador não realiza a
  validação de verbas já quitadas na rotina de Valores Futuros
type: support-article
updated_at: '2026-05-19T14:53:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35816163879191-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-Cr%C3%A9dito-do-Trabalhador-n%C3%A3o-realiza-a-valida%C3%A7%C3%A3o-de-verbas-j%C3%A1-quitadas-na-rotina-de-Valores-Futuros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35816163865111) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
 Importação Crédito do Trabalhador não realiza a validação de verbas já quitadas na rotina de Valores Futuros  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**

1. Verifique a versão do sistema atualmente em uso.
2. Atualize o ambiente do Protheus, conforme links abaixo (selecione apenas o link relacionado a versão do seu Sistema).
   1. Versão **12.1.2310**: <https://suporte.totvs.com/portal/p/10098/download?e=1123885> >> **SOMENTE PARA CLIENTES COM GARANTIA ESTENDIDA**
   2. Versão **12.1.2410**: <https://suporte.totvs.com/portal/p/10098/download#detail/1170810>
   3. Versão **12.1.2510**: <https://suporte.totvs.com/portal/p/10098/download?e=1221795>

O sistema realiza a validação de verbas que estão em uso na rotina valores futuros (SRK). Caso já exista uma verba registrada na rotina, que esteja com o campo Situação igual a Descontinuado ou Pago, o sistema vai reutilizar essas verbas para novos empréstimos.

* Realizado ajuste para reutilização de verba usada em empréstimo pago ou com status descontinuado.

**Saiba mais:**

[eConsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)

[Manual Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)  
<https://tdn.totvs.com/pages/releaseview.action?pageId=1007090850>
