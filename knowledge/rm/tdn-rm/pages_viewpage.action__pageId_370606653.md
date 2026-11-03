---
content_hash: 07faddb10cfe41608177d7664ac3498208ae18ff9e0d312cf0c27fc1a4e373ee
fetched_at: '2026-06-29T00:09:00.862408+00:00'
page_id: '370606653'
product: rm
source: tdn-rm
title: 2850166 FISCAL01-4638 DT Adequação da DAPI/MG referente ao novo layout 9.00
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370606653
version: 84
---

# Adequação da DAPI/MG referente ao novo layout 9.00

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Rotinas Estaduais - DAPI-MG |
| **Situação/Requisito:** | Cliente solicita adequação da DAPI referente ao novo layout 9.00. |
| **Solução/Implementação:** | Implementações VERSÃO 9.00.00 – Rotina DAPI\MG  Criado na Tela de Geração da Rotina DAPI\MG o Campo - “Desconto ICMS – Decreto 47.226/2017”.  Com as seguintes Opções: 0 - Não se Aplica 1 - 1% 2 - 2%  Se o campo estiver preenchido com 1 ou 2%, então na geração da Rotina o Campo  “Termo de Aceite” do Registro 00 posição 60 recebe “S”,  se estiver preenchido com Não se Aplica recebe “N”. O Valor informado no campo deve ser gerado na Linha Tipo 10:  Linha Tipo 10 Identificação 131 (99.2 ICMS A Recolher). Deve ser gerado conforme: Identificação 99 (ICMS ICMS a Recolher) -  Identificação 130 (Desconto ICMS 1% ou 2%)  Observações: 1 - Se o campo novo "Desconto ICMS" da tela de  geração da Rotina, estiver zero "Não se Aplica" o Campo Identificação 131 deve receber o valor do Campo Identificação 99 (ICMS a Recolher).  2 - Os campos Identificação 130 e 131 so devem ser gerados se o campo Identificação 99 for maior que zero. |
| **Issue:** | FISCAL01-4638; FISCAL01-4621 |

divs
