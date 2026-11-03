---
content_hash: 1248f4f8a481e9c85932cfb28e7b4270d7b73b7cb047882c861f896569e2ae14
fetched_at: '2026-06-29T00:06:30.054094+00:00'
page_id: '235310382'
product: rm
source: tdn-rm
title: TTJGZ8_DT_Ajuste_no_Cancelamento_de_Guias
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJGZ8_DT_Ajuste_no_Cancelamento_de_Guias
version: 118
---

# Ajuste no cancelamento de guias

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Atendimento | Registro de atendimento | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle e SQL Server |

## Descrição

Implementada rotina para cancelamento das guias da versão 3.0 da TISS.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.10.100 da biblioteca do RM.

## Procedimento para Utilização

1. Configure um WebService de cancelamento de guia nas Condições Contratuais do Convênio.
2. Em seguida, cadastre um registro de atendimento externo para qualquer paciente.
3. - Na aba **Guia/Autorização**, cadastre uma nova guia.
4. - Em seguida clique em **Cancelar** para cancelar a guia.
5. - Se o WebService estiver no ar, a guia solicitada será cancelada no sistema.

divs
