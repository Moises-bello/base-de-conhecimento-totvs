---
content_hash: 5d557d5b49d7823a8432f219e8a0121470d5206b0250c679eca2ccd26c5e321f
fetched_at: '2026-06-29T00:10:11.155271+00:00'
page_id: '452719954'
product: rm
source: tdn-rm
title: Eventos de Média
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719954
version: 3
---

Esta pasta define se o evento deve integrar ao cálculo das médias de Férias, 13º Salário, Aviso Prévio , Licença Maternidade, Férias Rescisão, 13º Rescisão.   
    
 Através do cadastro é possível controlar:

* **Pasta Identificação**

Grupo 0 (zero): O valor calculado da média será lançado no mesmo evento onde serão pagas as Férias, 13º Salário, Aviso Prévio, Licença Maternidade, ou seja sem discriminação de médias.   
 Grupos Um(1) a dezenove(19): O valor calculado da média será ançado em separado, neste caso, ocorrendo à discriminação das médias. Veja nas pastas de Médias de Férias, 13º Salário, Aviso Prévio e Licença Maternidade em Cadastros | Sindicatos.

**Atenção**  
 Para o tipo de média "Incide Salário Maternidade", o sistema permitirá que seja selecionado somente o Grupo 0 ou 1.

**Observação**  
 1) Os eventos que compõem comissão não podem fazer parte dos eventos de média.

2) Se o usuário optar por utilizar médias (Cadastros | Sindicatos) e desejar que o cálculo da média seja lançado separado dos eventos de férias, deverá preencher o campo "Grupo" (Cadastros | Sindicatos| pasta deMédias). Deve ser informado um código numérico definindo um grupo a que o evento pertencerá.

O evento com código de cálculo 038 (Férias) deverá pertencer ao "grupo 0". Nos grupos de 1 a 5, poderá ser informado o código do evento que agrupará os valores da média de férias. Estes eventos deverão ter as mesmas incidências do evento de código de cálculo 038, porém sem código de cálculo.

Caso não deseje trabalhar com grupo de média, deverá informar somente o grupo 0 (zero) para o evento com código de cálculo 038 (Férias). Neste caso, os valores das férias e da média virão concentrados no evento de código de cálculo 038 (Férias).

O cálculo do INSS de férias será proporcionalizado segundo o número de dias de férias gozados pelo funcionário no mês.

**Exemplo**  
 Os eventos que participarão da média deverão incidir férias nos respectivos grupos:   
 *Código         Descrição                 Incide Férias          Grupo*  
 080           Hora Extra 50%                 Sim                   01  
 090           Hora Extra 100%               Sim                   01  
 091           Gratificação                       Sim                   02  
 092           Gratificação Especial          Sim                   02

O mesmo processo (de grupamento) pode ser usado no cálculo da diferença de férias. O evento da diferença da média deve ser específico, separado do código de cálculo 045 - DIF. FÉRIAS PAGAS NO MÊS. Para esse evento, você deverá informar o grupo "0" o evento com código de cálculo 045 - DIF. FÉRIAS PAGAS NO MÊS. Os grupos de 1 a 19 deverão ser preenchidos conforme sua necessidade.

Os eventos que concentrarão os valores da diferença de médias NÃO poderão ter código de cálculo.

Os valores das diferenças de médias aparecerão embutidos nos valores dos eventos com código de cálculo 045 - DIF. FÉRIAS PAGAS NO MÊS e código de cálculo 080 - DIF. FÉRIAS PRÓX. MÊS caso não existam distribuição por grupos.

**Último Valor**  
 O campo "Último Valor" deve ser selecionado se o usuário desejar, que em lugar das médias de valores do evento, o sistema considere o último lançamento conforme parametrizado no sindicato.
