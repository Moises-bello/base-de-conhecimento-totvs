---
article_id: 360022161132
category: Materiais - Compras (SIGACOM)
content_hash: e6788459d3f6f66f43bbe89ac33da8c5370d22549058ccc9f0cfadcb29520d3d
fetched_at: '2026-06-28T22:41:09.007700+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Lentidão ao incluir
  documento de entrada com Ativo
type: support-article
updated_at: '2024-02-08T19:47:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022161132-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Lentid%C3%A3o-ao-incluir-documento-de-entrada-com-Ativo
---

**Ocorrência**Ao incluir um Documento de Entrada (MATA103), onde existe integração com Ativo, o sistema apresenta lentidão em alguns casos demorando horas para concluir o processo após clicar no botão salvar.

**Ambiente**  
Protheus – Compras – A partir da versão 12.1.17   
  
**Causa**Houve melhorias de performance referente a esta integração e hoje uma possibilidade referente a lentidão, pode ser tratada conforme as indtruções contidas no item "Solução" abaixo:

**Solução**  
Para solucionar essa ocorrência como saída de contorno, realize os seguintes passos:

1 – Ao dar entrada no Documento de entrada(MATA103), deve-se cadastrar uma nova TES utilizando a configuração abaixo:

Atualiza ativo=SIM (F4\_ATUATF) e Desmembra itens no ativo=Não (Desme.IT.ATF , F4\_BENSATF)

 OBS: Ao informar “Não” no campo Desme.IT.ATF, o sistema deverá criar apenas um registro no ativo fixo com a quantidade informada.

Ou seja se em uma situação onde for igual a **SIM**, quando for lançado um item com quantidade 10 na NF, será gerado 10 itens com quantidade igual a 1 no Ativo Fixo e com isso causará lentidão.

Se igual a **NÃO** será gerado apenas 1 item com quantidade igual a 10. Este parâmetro só terá efeito se o campo "Atual.Ativo "F4\_ATUATF" for igual a **SIM**.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
