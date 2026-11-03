---
article_id: 16136713672343
category: RH - Provisão
content_hash: 6e0077433744db58cd20210f22e989b01852b0104684af17a87841022c350a7b
fetched_at: '2026-06-28T22:43:55.945598+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Manual das Provisões de Férias e 13º Salário
type: support-article
updated_at: '2025-06-18T18:04:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16136713672343-RH-Linha-Protheus-GPE-Manual-das-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16136729272471) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como Parametrizar/Processar os Cálculos de Provisão de Férias e 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O cálculo de provisões tem como principal objetivo, gerar os valores de Provisão de Férias e 13º Salário para a contabilidade.

A partir do campo "Dt. Bas. Fer" (data que indica o início do período aquisitivo do funcionário) será calculada a provisão de férias que atualizará este cadastro mês a mês com as informações de dias e faltas de férias vencidas, dias e faltas de férias proporcionais e valor da 1ª. parcela do 13º. Salário.

A rotina de Calculo efetiva o cálculo das provisões de Férias, 13º salário, 14º salário e PLR.   
Após o cálculo, são gerados os lançamentos segundo um critério de apuração de valores nas verbas correspondentes aos identificadores de cálculo.

Para prosseguir com os Cálculos das Provisões, é necessário realizar as configurações abaixo:

**1. Passo.** Configuração de Verbas:  
Para acessar os identificadores de cálculo das verbas de Provisão [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6071282481303-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-identificadores-de-c%C3%A1lculo-dispon%C3%ADveis-para-provis%C3%A3o-de-f%C3%A9rias-e-13o-sal%C3%A1rio).  
**Importante:** Todas as verbas devem ser cadastradas com o Tipo 3-Base Provento e sem nenhuma incidência.

**2. Passo**. Parâmetros Específicos:

**P\_PROVAVP**: indica se provisiona as férias e 13º sobre o aviso indenizado. Para mais informações [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012920611-MP-GPE-Como-o-provisionar-o-d%C3%A9cimo-e-f%C3%A9rias-sobre-o-aviso-pr%C3%A9vio-indenizado)

**MV\_CSALINC**: indica o Ano/Mês inicial de utilização das verbas de salário incorporadas ao cálculo das provisões. Para mais informações [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11899851782423-RH-Linha-Protheus-GPE-Conceito-do-Par%C3%A2metro-MV-CSALINC-)

**MV\_PROVRES:** possibilita ao usuário a opção de escolha entre apurar ou não o provisionamento de Férias e Décimo Terceiro Salário no mês de demissão do empregado. Para mais informações [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007260472-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Provis%C3%A3o-no-m%C3%AAs-de-Desligamento)

**MV\_TPBXFER:** possibilita ao usuário a opção de escolha entre efetuar a baixa do pagamento das férias integralmente no recebido das férias ou conforme os períodos de gozo. PAra mais informações [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024752653-RH-Linha-Protheus-GPE-Ferias-partidas-na-provis%C3%A3o-par%C3%A2metro-MV-TPBXFER)

**MV\_TRFAMES:** indica o Ano/Mês inicial de utilização da nova forma de demonstração das transferências. Para mais informações [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025027553-RH-Linha-Protheus-GPE-Como-Conferir-os-Relat%C3%B3rios-de-Provis%C3%A3o-com-Transfer%C3%AAncia-)

**MV\_RATPROV:** Possibilita ao usuário calculas as provisões rateadas por centro de custo, item contábil ou classe valor.Para mais informações [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028664711)

**3. Passo:** Cálculo das Provisões.  
Para mais informações sobre como processar os cálculos das Provisões  [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004784961-RH-Linha-Protheus-GPE-Como-efetuar-c%C3%A1lculo-da-provis%C3%A3o-)

**4. Passo:** Cálculo de Provisão de 14º Salário:  
A provisão de 14º salário possui um tratamento diferenciado, pois acompanha o cálculo da provisão de 13º salário.   
Para que o cálculo seja efetuado, basta informar, no momento do cálculo da provisão de 13º salário, o percentual de 14º. Esse percentual é aplicado sobre o cálculo do 13º e apresentado em forma de lançamentos no relatório, bem como na manutenção de lançamentos.  
Para mais ifnromações [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058496694-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-14%C2%BA-sal%C3%A1rio-na-provis%C3%A3o)

**5. Passo.** Cálculo de Provisão de PLR:

Por padrão, o Protheus não realiza Cálculo de Provisão de PLR, por serem valores definidos de acordo com a Convenção Coletiva da Categoria dos funcionários, configurados no Cadastro de Sindicato.  
Foi disponibilizado o Ponto de Entrada **GP070PLR**para esta tratativa.  
Para mais informações [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044606833-RH-Linha-Protheus-GPE-Provis%C3%A3o-de-Participa%C3%A7%C3%A3o-nos-Lucros-PLR-GP070PLR-#:~:text=Como%20calcular%20Provis%C3%A3o%20de%20Participa%C3%A7%C3%A3o%20nos%20Lucros%20%2D%20PLR%3F&text=Por%20padr%C3%A3o%2C%20o%20Protheus%20n%C3%A3o,configurados%20no%20Cadastro%20de%20Sindicato).

**6. Passo:** Conferência do Relatório de Provisão:

A emissão do relatório de Provisão exibe diversas informações que influenciam no resultado apresentado. No início de impressão é apresentado dados relativos ao cálculo, que representa a quantidade em Dias correspondente à cada Valor demonstrado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16136504351639)

**Observação:** A linha vertical em azul NÃO existe no relatório original. Foi utilizada para uma melhor demonstração. 

**Anterior**-> para esta linha não existe cálculo algum; o sistema apenas transporta o valor encontrado no SRT do cálculo anterior.

**Mês**-> será sempre a diferença entre o Atual - Anterior

**Atual**-> é efetuado o cálculo com referência na Data Base de Férias X Data de Cálculo.

**Valor** → nesta coluna será apresentado a provisão referente a parte fixa (salário).

**Adicionais**-> nesta coluna será apresentado a provisão referente a parte variável (média).

**1/3 Constit.** -> nesta coluna será apresentado a provisão referente à 1/3 da parte total (fixa + média).

**Total Ferias** -> Valor total, somatória de Valor + Adicionais + 1/3.

**I.N.S.S**. → percentual definido na tabela S037 e S038 aplicado sobre o Total de Férias.

**F.G.T.S.** -> percentual definido no parâmetro S037 e S038.

**Total Encargos** -> somatória de I.N.S.S. e F.G.T.S.

**Total Geral** -> somatória de Total Férias e Total Encargos

**Saiba Mais:**   
[Manual da Provisão](https://tdn.totvs.com/pages/releaseview.action?pageId=754967312)
