---
content_hash: 7065b62e0ff5e7f551c5f3726e0ce06b0393c2515af15a00592ebac2b963cedb
fetched_at: '2026-06-29T00:09:59.847486+00:00'
page_id: '452718418'
product: rm
source: tdn-rm
title: Informações complementares do Participante
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718418
version: 2
---

**Informações complementares do Participante**

Por este anexo é possível inserir uma sentença SQL para que traga informações do participante a ser visualizado na avaliação de desempenho no Portal pelo avaliador.

 A consulta SQL cadastrada no RM é visualizada na avaliação de desempenho correspondente no Portal, devendo selecionar o avaliado a que se deseja consultar os dados para responder e ir em *Informações do Avaliado*, no topo da tela de responder à AD.

 Para inserir uma consulta SQL, é preciso selecionar a avaliação de desempenho a qual se deseja consultar informações do avaliado e ir em *Anexos | Informações Complementares do Participante* e incluir a Consulta SQL desejada.

 É preciso atentar que para o correto funcionamento da consulta SQL

O *WHERE* deve ser igualado à **:CODCOLIGADA** e **:CHAPA** e o *SELECT* deve comtemplar os campos **CHAPA** e **CODCOLIGADA**. Os parâmetros **:CODCOLIGADA** e **:CHAPA** devem ser colocados na ordem que são apresentados na consulta a seguir.  
   
*SELECT CHAPA, CODCOLIGADA* *FROM PFUNC (NOLOCK)* *WHERE* *CODCOLIGADA = **:CODCOLIGADA*** *AND* *CHAPA = **:CHAPA***  
   
 Esses dados são o básico para realizar a consulta de informações complementares do participante, à partir do mesmo é possível consultar toda a informação do avaliado que julgar necessário para uma melhor avaliação de desempenho pelo avaliador.  
    
Voltar
