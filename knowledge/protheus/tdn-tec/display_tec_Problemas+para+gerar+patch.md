---
content_hash: 8f846a0005835e68d2b3291eb882bee08b8b80d90602272e6d22381815be32de
fetched_at: '2026-07-02T19:24:19.815391+00:00'
page_id: '244432645'
product: protheus
source: tdn-tec
title: Problemas para gerar patch
type: documentation
url: https://tdn.totvs.com/display/tec/Problemas+para+gerar+patch
version: 1
---

Durante a geração de patch "por recursos selecionados a partir da Area de trabalho" com a opção "Verificar arquivos no RPO" os arquivos de pastas marcadas para "Ignorar compilação" estavam sendo considerados

|  |  |
| --- | --- |
| Situação | Os arquivos nas pastas marcadas para "Ignorar compilação" normalmente não estavam no RPO e portando não podiam ser adicionados ao patch a ser gerado. |
| Ocorrência | Problemas para gerar patch |
| <Tipo de alteração (correção, implementação, melhoria, homologação)> | O processo de seleção de recursos para inclusão na arvore para escolha de arquivos foi revisto e agora desconsidera as pasta marcadas para "Ignorar compilação". |
| Informações adicionais | * Referente ao chamado: TVIPK7 * Referente à ocorrência: SSIM-1153 * Disponível em builds superiores a 11.3.2 |
