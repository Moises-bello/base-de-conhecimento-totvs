---
content_hash: 52e2cb1b3aff6ea9704575c22ba2e5b70b6ca0ac3df727b72e73368457554ea7
fetched_at: '2026-06-29T00:09:14.191789+00:00'
page_id: '421385147'
product: rm
source: tdn-rm
title: Ajuste de Grupos DNIT
type: documentation
url: https://tdn.totvs.com/display/LRM/Ajuste+de+Grupos+DNIT
version: 2
---

Através deste assistente pode-se acertar o grupo DNIT dos insumos ou recursos de composições.  
 O grupo DNIT será ajustado para os insumos que possuem grupo DNIT diferente do grupo DNIT do seu grupo de custo, insumos que não possuem grupo de custo, recursos de composições que não são por produção e que possuem grupo DNIT diferente de nulo e recursos insumos que estão associados a composições por produção e que possuem grupo DNIT diferente de nulo.

**Exemplos**  
Grupo DNIT do insumo, diferente do grupo DNIT do seu grupo de custo:  
O insumo M00010 possui grupo DNIT E, mas seu grupo de custo possui o grupo DNIT A.  
Caso exista, será alterado o grupo DNIT do insumo e grupo de custo para o grupo DNIT informado no campo "Novo Grupo de Custo".  
Insumos que não possuem grupo de custo:  
O insumo M00036 não possui grupo de custo relacionado.  
Caso exista, será incluído o grupo de custo informado para o insumo em questão.  
Recursos insumos que estão associados composições que não são por produção e que possuem grupo DNIT diferente de nulo:  
Recurso M00040 associado a composição que não é por produção 000001 que possui grupo DNIT igual a E. Esse recurso deveria possuir o grupo DNIT igual a nulo.  
Caso exista, será colocado nulo para o grupo DNIT deste recurso.  
Recursos insumos que estão associados a composições por produção e que possuem grupo DNIT diferente de nulo:  
Recurso M00061 associado a composição por produção 500000 que possui grupo DNIT diferente de nulo. Esse recurso deveria possuir o grupo DNIT igual a nulo.  
Caso exista, será colocado nulo para o grupo DNIT deste recurso.

Para projetos que possuem posição igual a Paralisado ou Concluído ou Revisado ou Cancelado não será possível efetuar o ajuste de grupos DNIT.
