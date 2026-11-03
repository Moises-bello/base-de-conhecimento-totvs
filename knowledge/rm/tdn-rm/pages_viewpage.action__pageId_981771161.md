---
content_hash: ce405b3a883c050919ba05a90acf3af887592082b111cdfa28f366865874c4ab
fetched_at: '2026-06-29T00:12:15.678102+00:00'
page_id: '981771161'
product: rm
source: tdn-rm
title: FISCAL01 - 26677 - EFD Contribuições - Registro F200 - Conteúdo do campo inválido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981771161
version: 3
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | EFD CONTRIBUIÇÕES |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01 - 26677 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o arquivo txt da rotina **EFD Contribuições** , é apresentada a seguinte inconsistência no log:  
   
   
*Registro F200. Erro ao gravar valor do campo VL\_COFINS. Valor: '2100000,000000000000'. Erro: O valor excedeu o tamanho do campo e foi truncado.*  
*Geração concluída. Duração: 0:0:13,97*  
   
Como consequência, ao importar o arquivo para o **validador** , ocorre erro de estrutura no registro **F200** , campo **VL\_COFINS** :  
   
Mensagem: *Conteúdo do campo inválido.*  
   
Observação: A empresa possui menos de 6 meses em exercício.

## **03. SOLUÇÃO**

Ajustado e liberado novo layout para EFD Contribuições.

Alteração no tamanho do campo VL\_COFINS para aceitar apenas 2 casas decimais.

Disponível à partir da biblioteca 12.1.2410
