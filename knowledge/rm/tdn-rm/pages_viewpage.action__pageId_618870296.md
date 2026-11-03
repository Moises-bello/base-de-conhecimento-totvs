---
content_hash: 06472ff6a08a18522baad7b45b1534aacfe678ff64116eae7150f1b48deb172b
fetched_at: '2026-06-29T00:11:02.502771+00:00'
page_id: '618870296'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - SPED Fiscal - Geração Bloco F200 - Empreendimento
  TCGI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=618870296
version: 24
---

O documento tem por objetivo demonstrar a configuração básica necessária para a geração do bloco F200 no arquivo SPED a ser gerado pelo gerador de saídas, através do Layout fornecido pela TOTVS. Com foco na demonstração de apresentação do desconto condicional e incondicional para empreendimentos do TCGI.

Importante:

* **O campo "F200 Tipo Regime de Tributação", utilizado para controlar o somatório ou não de desconto condicional, se encontra disponível a partir da versão 12.1.32 ou superior.**
* O Embasamento técnico para implementação da nova funcionalidade para distinção de valores incondicionais ou condicionais, onde o mesmo compõe ou não o valor de baixa total a ser apresentado no arquivo para o bloco F200, se encontra na consultoria:
* Sugestão de **[SQLs](https://tdn.totvs.com/display/LRM/SQLs+para+validar+Sped+F200+e+RET1800)** para validar valores do SPED
* **Log do SPED** gera em ...\RM.NET\Arquivos\LOG\_SPED
* Para geração do EFD:
  + A filial deve estar preenchido no empreendimento;
  + No anexo da filial, os dados fiscal deve ter um registro inserido salvo;
  + Se a tributação "Apura pelo Regime Especial Tributação" estiver marcada, a data do habite-se esta preenchida e "Gerar registro 1800 da EFD independente da data habite-se" desmarcado, então não pode ter data de venda  anterior ao habite-se. Ou coloca a data antes da primeira venda, ou deixa o registro em branco ou desmarca a tributação do tipo RET;
  + Não pode esquecer de gerar o contrato da venda que é obrigatório para o Sped.

**SPED Fiscal - Geração Bloco F200 - Empreendimento TCGI**

Descontos Condicionais / Incondicionais no Arquivo F200 do Sped Fiscal.

Abrir a visão de empreendimento ir na aba EFD-Pis/COFINS,   
preencher os campos do bloco F200. **Abaixo tem uma imagem com sugestão dos valores.**

No empreendimento >> anexo >> Dados do Repasse Empreendimento:  
Se existir percentuais de repasse a parceiros os valores serão calculados considerando somente o valor do percentual de responsabilidade da incorporadora da coligada:

**Exemplo:** Coligada 1 - Empreendimento (Canto das Cotovias) → possui parceiro cadastrado com 10%, então o valor de venda apresentado no bloco F200 será somente 90% do valor.  
**Obs.:** No caso dos prints abaixo não teremos parceiros.

Sobre o parâmetro : F200 Tipo Regime de Tributação.

* 01 - Regime Especial de Tributação  --> (Considera apenas desconto Incondicional no F200 ) Não levando o Desconto do Financeiro para o valor total baixado.
* 02 - Lucro Presumido / Regime de Caixa / Apuração Cumulativa PISCOFINS  --> (Considera desconto Incondicional e Condicional no F200 ).

Após preencher os dados do bloco e verificar que não existe o repasse citado acima.

Deverá ser executado o processo de cópia dos dados do EFD para as subunidades, para garantir que estes estejam preenchidos também na subunidade, que é utilizada como referência na busca dos dados para preenchimento do bloco F200 do arquivo de sped. Esse processo pode ser selecionado no momento de gerar novas subunidades, assim como em processos da visão das subunidades.

Abrir a visão de Blocos >> Anexo >> SubUnidades >> Selecione as subunidades que irá receber a cópia de dados do EFD >> Menu superior da visão vá em “Processos” >> Atualizar em lote.

Abrirá o processo "Atualizar em lote", poderá avançar para a próxima etapa, no bloco “Atualizar PIS/COFINS ?” >> marcar a opção “Sim, com o PIS/COFINS do Empreendimento” >> Executar.  
Ao final do processo poderá visualizar na tela dos dados da subunidade que os valores foram copiados para a mesma.

Imagem acima: Subunidade atualizada com as informações do EFD-PIS/Cofins.

**Layout para geração do Arquivo F200.**

Agora precisamos verificar se o layout de geração do sped já se encontra importado no gestão fiscal, se já estiver, podemos gerar no fiscal o arquivo sped.

Modificar de módulo, vá em BackOffice >> Gestão Fiscal >>  Obrigações Acessórias >> Gerador Saídas clique e abra a visão:  
Verificar se existe algum layout importado com o nome “EFD\_CONTRIBUICOES\_B”.

Caso não exista, você poderá importar o mesmo em: Processos >> Importar Layout >> Adicionar Objetos >> procurar na pasta da instalação do RM a pasta ‘Objetos Gerenciais/Layout’, encontrar o layout “FISLAY0006-EFD\_CONTRIBUICOES\_B.TotvsGen” 

Após importar o layout para o gerador de saídas que será utilizado na geração do arquivo sped.  Iremos parametrizar a tela do processo com os dados necessários para a geração e gerar o arquivo. segue print com sugestão de valores para os campos.

Selecione o layout importado, “2 - EFD\_CONTRIBUICOES\_B” vá em Processos >> Geração de Saídas.

Para gerar o Arquivo F200 .

* **Desconto Incondicional (TCGI)**  
  Utilizando a parametrização do campo "F200 Tipo Regime de Tributação":  
  (Sem Valor ou  01 - Regime de Tributação Especial )

**Exemplo para geração do Arquivo F200 com Tipo de Regime de Tributação ( 01 - Regime de Tributação Especial )**

*Visão da venda com a "Condições de financiamento" tendo o componente de desconto incondicional já incluído.*

Valor Original da Parcela              = 15.000 Reais   
Valor do Desconto Incondicional =      100 Reais por parcela  
Total do Desconto Incondicional  =   1.000 Reais nas 10 Parcelas.Valor Total da Venda = Valor Subunidade - Valor Total do Desconto Incondicional  
Valor Total da Venda = 150.000 - 1.000 = 149.000

Valor da parcela = Valor componente original - Desconto Incondicional  
Valor da parcela = R$ 15.000 - R$ 100 = R$ 14.900  
  
A imagem abaixo demonstra o valor total da parcela já com o desconto incondicional e agora será acrescentado mais um desconto condicional de R$ 10 no momento da baixa.  
Valor da parcela = R$ 14.900 - R$ 10 = R$ 14.890

*Neste caso dos R$ 10,00 de desconto condicional e com o parâmetro "F200 Tipo Regime de Tributação" definido como (Sem valor ou RET) o valor do desconto condicional será incluído como total recebido pela incorporadora. Vejamos isso abaixo no arquivo gerado.*

Gerando arquivo F200

Informar Coligada e Filial

Informar Período da Baixa (Data Inicial e Data Final).

Informar Rotina | Classificação de Municípios | Classificação de Países | Classificação de Países ( Comércio Exterior )

**Após configurar os parâmetros ( Avançar e Executar em seguida. )**

**Localizar o arquivo gerado e abrir.**

*Valor total baixado considerando apenas o desconto incondicional da parcela para o período do arquivo gerado.   
Vermelho : Valor do Contrato**Verde : Valor da Baixa*

* **Desconto Condicional (TCGI)**  
  Utilizando a parametrização do campo "F200 Tipo Regime de Tributação":  
  (02 - Lucro Presumido / Regime de Caixa / Apuração Cumulativa PISCOFINS)

**Exemplo para geração do Arquivo F200 com Tipo de Regime de Tributação ( 02 - Lucro Presumido / Regime de Caixa / Apuração Cumulativa PISCOFINS)**

*Todas as parametrizações utilizadas no processo de geração podem ser utilizados novamente, o que se mudou neste momento é apenas a informação no cadastro de empreendimento relacionado ao campo "F200 Tipo Regime de Tributação" para '02 - Lucro Presumido / Regime de Caixa / Apuração Cumulativa PISCOFINS'.*

*Valor total baixado considerando agora o desconto incondicional e o desconto condicional da parcela para o período do arquivo gerado.  
Vermelho : Valor do Contrato**Verde : Valor da Baixa*

Importante:

**"Valor recebido, acumulado até o mês anterior ao da escrituração"** => considera o valor baixado observada a seguinte regra: se a data da baixa é anterior ao período do SPED representa valor apurado até o mês de escrituração, se a data da baixa está dentro do período do SPED representa o valor no mês de apuração.

**"Valor total da unidade imobiliária vendida"** => corresponde ao somatório de todos os componentes de todas as parcelas da venda observado o parâmetro do componente "Desconsiderar valor na exportação do SPED".

##### API para F200:

A partir da versão **12.1.2209** foi disponibilizado uma API para retornar os dados da F200. Para realizar o consumo da API é preciso utilizar o método POST informando a '<http://localhost:8051/api/imb/v1/efd/registryF200>'. Para que a API retorne informações o corpo da mensagem precisa ter o seguinte JSON:

 {   
     "CodigoColigada" :"1", – Código do Empreendimento  
     "CodigosFiliais" :[1,2],  – Lista de Filiais  
     "DataInicial" :"2000-01-01",  – Data Inicial  
     "DataFinal" : "2020-12-31"  – Data Final  
 }

Parâmetro Limitar Filtro Data

Novo parâmetro para limitar a busca do SPED com a data inicial e data final do processo com relação a vendas quitadas, trazendo que somente vendas quitadas no mês e vendas em andamento.

Parâmetros Gerais TCGI => Geral
