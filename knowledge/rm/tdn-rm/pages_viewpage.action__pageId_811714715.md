---
content_hash: 8ee2837e9a8cb89f26ab923883b7dde503aa0734284370ff2f718dc8d513474c
fetched_at: '2026-06-29T00:11:44.259258+00:00'
page_id: '811714715'
product: rm
source: tdn-rm
title: DT - S-1200 e S-1210 - Unificação de períodos mediante retificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=811714715
version: 9
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-1200 e S-1210 - Unificação de períodos mediante retificação |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | [DRHROTRM-8163](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8163) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2310.143
* 12.1.2306.210

## **03. SITUAÇÃO/REQUISITO**

Seguindo o parecer SEI Nº16120/2020, é preciso unificar a geração dos arquivos XML no eSocial. Isso ocorre porque não podemos enviar uma restituição de INSS sem incluir o desconto correspondente na mesma tag <ideDmDev>.

## **04. SOLUÇÃO**

Realizamos uma tratativa no produto incluindo o parâmetro '**Unificar período na retificação'**. Quando ativado, o sistema passa a unificar a geração dos XMLs de retificação, o que significa que os eventos registrados nos períodos de retificação são agora consolidados no período original.

Vale ressaltar que, por enquanto, essa atualização não abrange rescisões. Assim que essa funcionalidade estiver disponível, será registrada por meio de nossas documentações.

**O QUE FOI AJUSTADO?**

1) Após a liberação da versão será necessário executar os script's de adequação da tabela e dos campos do sistema através do sistema **RM.Atualizador.exe.**

2) Ative o parâmetro criado acessando o caminho: RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 5/7.

3) Proceda com o lançamento das retificações. O sistema irá registrar a qual período original a retificação está relacionada.

4) No XML S-1200, somente o <ideDmDev> original foi gerado. Os eventos do período de retificação 10000, conforme mencionado anteriormente no item 3, foram registrados no <ideDmDev>1, correspondente ao período original.

 

5) No XML S-1210, apenas o <ideDmDev>1 foi gerado, referente ao período original.

Importante!

1. Inicialmente, este parâmetro não unificará as retificações de rescisão.
2. É essencial executar o atualizador para garantir o correto funcionamento do processo de unificação, pois, a partir das versões mais recentes, os eventos com o mesmo código terão seus valores somados.

## **05.****DEMAIS INFORMAÇÕES**
