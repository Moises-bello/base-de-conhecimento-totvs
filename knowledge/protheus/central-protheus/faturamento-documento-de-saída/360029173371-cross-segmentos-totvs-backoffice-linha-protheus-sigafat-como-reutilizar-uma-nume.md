---
article_id: 360029173371
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: ac4ab3d4105cb4db741bf72e96359f9be9c95c974d4b3e6d33c61bfe0429adee
fetched_at: '2026-06-28T22:38:45.129972+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - Como reutilizar
  uma numeração de Documento de Saída
type: support-article
updated_at: '2023-07-19T12:45:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029173371-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-reutilizar-uma-numera%C3%A7%C3%A3o-de-Documento-de-Sa%C3%ADda
---

**Dúvida**

Como reutilizar uma numeração de Documento de Saída (**MATA461**)?

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - A partir da versão 11.80

**Solução**

Premissas para reutilizar numeração:

* Numeração transmitida para SEFAZ ou prefeitura não há como reutilizar;
* É necessário que a primeira nota tenha sido devidamente excluída na rotina **MATA521**; caso contrário, o sistema irá reconhecer que já há um Doc de saída com esse número, e irá utilizar o próximo disponível;
* Caso o parâmetro **MV\_TPNRNFS** esteja com conteúdo 3, ou seja, "Controle por **SD9**" o parâmetro **MV\_MUDANUM** tem que estar com o conteúdo **.T. (MV\_MUDANUM = .T.).**
* O usuário deve ter a opção 50 (Alterar Num da Nf. ) dentro do configurador como habilitado (Aba -Restrições de Acesso> Aba - Acessos). Caso o campo **Regra de acesso por grupo** estiver como **1- Priorizar** a opção 50 deve estar habitada no Grupo ao qual o usuário pertence dentro do configurador.
* Verifique se a numeração que deseja reutilizar consta no documento de entrada com formulário igual sim na rotina **MATA103**, pois significa que é o emissor da nota de entrada e que vai consumir uma numeração;
* Consulte se a numeração está deletada nas tabelas **SF2** e **SD2**, pois significa que o documento de saída está devidamente excluído.
* Consulte a numeração nas tabelas: **SFT** o campo **FT\_OBSERV** preenchido "**NF CANCELADA**" e **SF3** o campo **F3\_OBSERV** preenchido "**NF CANCELADA**", afim de verificar se a numeração está apta para reutilização.

**Procedimento para reutilização:**

1- Incluir o Pedido de Vendas, ou (se for o caso) reutilizar o Pedido antes utilizado;  
2- Clicar em Preparar o Documento de saída (Pode ser feito na Rotina **MATA460A** ou em **MATA410** > Ações relacionadas > Prep. Doc Saida);  
3- Após realizar as devidas avaliações de Liberação do Pedido, e após exibir tela de parâmetros, o sistema exibe uma janela em que demonstra o número da série e da Nota que será gerada;  
4- Nesta janela, localize a linha com a série, e dê 2 cliques sobre o número de Nota que é exibido;  
5- Neste campo o sistema permite editar a numeração, de forma a digitar manualmente o número que deseja utilizar.

**Saiba mais:  
[FAT0005 Reutilizar Numeração de Documento de Saída(NF)](http://tdn.totvs.com/pages/releaseview.action?pageId=225263579)**
