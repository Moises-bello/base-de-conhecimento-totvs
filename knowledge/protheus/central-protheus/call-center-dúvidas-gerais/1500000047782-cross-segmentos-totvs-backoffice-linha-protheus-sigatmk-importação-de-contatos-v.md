---
article_id: 1500000047782
category: Call Center - Dúvidas Gerais
content_hash: d56e33827ce8b98cab61812c6418968329d2a66f181002ae3d5f577336e78718
fetched_at: '2026-06-28T22:41:26.989772+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - Importação de Contatos
  via MILE através do Cadastro de Contatos TMKA070
type: support-article
updated_at: '2022-06-17T16:52:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000047782-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Importa%C3%A7%C3%A3o-de-Contatos-via-MILE-atrav%C3%A9s-do-Cadastro-de-Contatos-TMKA070
---

**Ocorrência**Ao realizar a configuração do Mile para importação dos Cadastros de Contatos (TMKA070) o sistema não conclui o processo de importação gerando, no log do Mile, a mensagem de erro:

type mismatch on compare  on MSROTAUTO(MATXFUNB.PRX)  
  
**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK – Faturamento – A partir da versão 12  
  
**Causa**Para realizar a importação dos dados na rotina de Contatos (TMKA070) incluindo o endereço e telefone utilizando o MILE, será necessário algumas configurações adicionais, pois atualmente a estrutura do MILE não permite realizar a importação utilizando simplesmente a configuração de canais.

**Solução**Para utilizar a ferramenta Mile na rotina de Cadastro de Contatos, siga as orientações da documentação: <https://tdn.totvs.com/x/BSMjIg>
