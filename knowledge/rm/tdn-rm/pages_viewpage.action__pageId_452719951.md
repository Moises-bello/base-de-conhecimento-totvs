---
content_hash: ef759176d4b1c77dd3c7b1abc6331cf23357641911b4894c0d817d1974e8ba83
fetched_at: '2026-06-29T00:10:11.142939+00:00'
page_id: '452719951'
product: rm
source: tdn-rm
title: Folha Analítica por Dissídio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719951
version: 8
---

### **Folha Analítica por Dissídio**

A Folha Analítica por Dissídio é um relatório que apresenta os valores referentes às diferenças salariais calculadas em decorrência de dissídio coletivo.

Esses valores são refletidos na Ficha Financeira do funcionário, acessível pelo caminho: Administração de Pessoal | Cadastros | Funcionários | Ficha Financeira | Verbas geradas por diferenças.

**Observação:**  
Somente serão consideradas no relatório as verbas cujo valor na coluna "Dissídio" seja igual a 1.

Portanto, sempre que aplicável, é fundamental marcar corretamente nos parâmetros de cálculo que a diferença salarial é decorrente de dissídio, garantindo que os dados sejam refletidos corretamente na Folha Analítica por Dissídio.

   
**Quebra de Seção**  
Permite filtrar as seções que serão consideradas na Folha Analítica por Dissídio, selecionando uma seção específica de acordo com seu código ou utilizando uma determinada quebra de seção.

**Seleção de Funcionários**  
Permite filtrar os funcionários lotados nas seções referentes à quebra de seção escolhida. O filtro pode ser de acordo com a 'Situação', 'Tipo de Funcionário' e/ou 'Recebimento'.

**Competência**  
Permite selecionar para qual competência a Folha Analítica por Dissídio será gerada, assim como o período.

⚠️ **Atenção:**

Ao selecionar uma competência anterior à atual, o sistema considera aúltima situação registrada para cada funcionário naquela competência, com base em seu histórico de situações.

Durante o processo deLiberação de Competência, as situações dos funcionários que retornaram ou saíram de férias (**F-Férias**) ou que estão afastados por um dos motivos abaixo são atualizadas conforme as movimentações ocorridas no período:

* + `P` - Afastamento Previdenciário
  + `T` - Acidente de Trabalho
  + `O` - Doença Ocupacional
  + `M` - Serviço Militar
  + `L` - Licença sem Vencimentos
  + `E` - Licença Maternidade
  + `R` - Licença Remunerada
  + `I` - Aposentadoria por Invalidez
  + `U` - Outros
  + `S` - Mandato Sindical
  + `W` - Licença Maternidade Complementar (180 dias)
  + `Y` - Licença Paternidade

Dessa forma, um funcionário que estava anteriormente em situação de afastamento poderá ser atualizado para **A-Ativo**, ou o contrário, após a execução do processo.

👉 Por esse motivo, ao gerar a Folha Analítica de competências retroativas, é essencial verificar o filtro de situação utilizado. Alguns funcionários que antes apareciam como afastados (ou ativos) podem não atender mais ao filtro configurado, impactando os resultados exibidos no relatório.

**Ordem**  
Permite selecionar se os funcionários recuperados serão apresentados no relatório por ordem de 'Chapa', 'Nome' ou 'CPF' (o valor padrão é 'Chapa'). Essa ordenação é aplicada após ordená-los por coligada, em seguida por categoria e, finalmente, por seção.

**Chaves Ativas**  
Permite filtrar quais eventos serão considerados no relatório de acordo com o valor de 'Chave' associado a cada um deles no seu respectivo cadastro (Administração de Pessoal | Cadastros | Eventos | Eventos). Caso nenhuma chave seja selecionada, os eventos não serão filtrados por chave.

**Código do Relatório (PDF)**  
Permite selecionar o layout que será utilizado para a geração do relatório em PDF.

**Código do Relatório (TXT)**  
Permite selecionar o layout que será utilizado para a geração do relatório em TXT.

**Formato de saída do relatório**  
Permite selecionar se o relatório será gerado em PDF ou TXT.  
   
**Localização do(s) arquivo(s)**  
Permite selecionar um diretório para armazenar o(s) arquivo(s) de relatório gerado(s) pelo processo.

**Parâmetros**

Os parâmetros **"Imprimir incidências dos eventos"** e **"Imprimir seleção do relatório"** permitem ao usuário definir se essas informações complementares serão exibidas no relatório:

* **Demonstrativo de Incidência:** apresenta o detalhamento das incidências dos eventos considerados no relatório (como INSS, IRRF, FGTS, etc.);
* **Seleção deste Relatório:** exibe os parâmetros de filtragem utilizados para gerar o relatório, como critérios de seleção de funcionários, períodos e eventos.

falseATENÇÃO:

O valor do evento com o código de cálculo **"373-****13º Rescisão Licença Maternidade Provento"** é utilizado nas seguintes bases:

* **Base INSS:** representa o somatório dos eventos que incide em INSS e INSS13 menos os eventos que estornam INSS e INSS13;
* **Base INSS Dissídio:** representa o somatório dos eventos que incidem em INSS e FGTS menos os eventos que estornam INSS e FGTS.
* **Base INSS Dissídio 13º:** representa o somatório dos eventos com código de cálculo 109, 412 ou código de cálculo 71 ou 220 que incidem em INSS13 e FGTS13.

O campo "Base Dif. Lic. Maternidade" considera apenas o evento com código de cálculo 17, pois esse evento possui incidência exclusiva do segurado e, portanto, não é incluído nas demais bases.
