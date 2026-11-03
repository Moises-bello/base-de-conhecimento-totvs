---
content_hash: 2a480a96d8cb532c4127309c12e40a4f82ecefa81608f816a6d12e6ca670c53d
fetched_at: '2026-06-29T00:05:48.593111+00:00'
page_id: '1025243125'
product: rm
source: tdn-rm
title: Município de Incidência Integrado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1025243125
version: 3
---

Para a NFS-e Nacional Ajuste da Alíquota do Tributo ISS retornada pela Prefeitura.

Quando na Consulta da NFS-e Nacional a Prefeitura Retornar a Tag: **pAliqAplic,**este valor será atualizado no Movimento

Faturado.

<valores>  
  <vBC>2530.00</vBC>  
  **<pAliqAplic>5.00</pAliqAplic>**  
  <vISSQN>126.50</vISSQN>  
  <vTotalRet>325.60</vTotalRet>  
  <vLiq>2204.40</vLiq>  
</valores>

Movimento RPS envio 2.1.x, deve estar com o campo Alíquota de ISS Zerado.

Obs.: Está Alíquota será zerada pelo serviço de Tributação quando o Municipio do Serviço estiver com o Parâmetro "Data Ativação da NFS-e Nacional" Preenchido:

Neste caso o Movimento 2.2.x, vai receber no Tributo ISS o Valor da Alíquota  que retornou da Prefeitura:

Obs.:  A Filial NÃO pode estar configurada como a opção "Optante pelo Regime Simplificado".
