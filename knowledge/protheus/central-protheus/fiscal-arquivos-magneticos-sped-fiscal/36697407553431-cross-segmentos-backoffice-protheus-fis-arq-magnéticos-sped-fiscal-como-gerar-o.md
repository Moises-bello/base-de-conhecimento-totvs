---
article_id: 36697407553431
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: ab6a21485414b60e72a6a58e4882371118b5f68162e236d9bc1076c87161091a
fetched_at: '2026-06-28T22:42:01.225768+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Sped Fiscal
  - Como gerar o registro D700 no arquivo do Sped Fiscal.
type: support-article
updated_at: '2025-12-01T21:58:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36697407553431-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Como-gerar-o-registro-D700-no-arquivo-do-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36697407541655) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como gerar o registro D700 no arquivo do Sped Fiscal.  
  
**Ambiente:**  
Microsiga Protheus – Livros fiscais – A partir da versão 12.1.2410.  
  
**Solução:**

O **registro D700** é utilizado para registrar as **Notas Fiscais de Comunicação - NFCom (Modelo 62)**de **Entrada** e **Saída**.   
A escolha entre **escrituração individualizada** ou **consolidada** depende das regras da **UF (Unidade Federativa).**

1. **Notas de Saída Normais (Individualizadas)**:
   * **Notas de saída** emitidas com a **tag "finalidade de emissão" igual a 0** (nota fiscal normal) devem ser escrituradas no **registro D700** se a **escrituração individualizada** for permitida ou exigida pela legislação da **UF (Unidade Federativa)**.
2. **Notas de Saída Consolidada**:
   * Quando a legislação da **UF (Unidade Federativa)** exigir a **escrituração consolidada** das **notas de saída**, essas devem ser registradas no **registro D750**.   
     Nesse caso, somente as notas de entrada, substituição e ajuste são escrituradas individualmente no registro **D700**.
3. **Notas de Entrada, Substituição e Ajuste**:
   * As **notas de entrada**, **substituição** e **ajuste** devem ser registradas individualmente, utilizando o **registro D700** (para escrituração individualizada) ou o **registro D750** (para escrituração consolidada), conforme exigido.

Quando houver a operação com o **Fundo de Equalização da Contribuição de Serviço de Comunicação (FECP)** no **documento fiscal**, são necessários dois registros filhos para registrar os valores corretamente:

* **Registro D731**:  
  Utilizado para **documentos escriturados de forma individualizada**. Se a nota fiscal de saída for escriturada individualmente (no **D700**), o valor do **FECP (****Fundo Estadual de Combate à Pobreza****)** deve ser registrado no **registro D731**.
* **Registro D761**:  
  Utilizado para **documentos escriturados de forma consolidada**. Se a nota fiscal de saída for consolidada (no **D750**), o valor do **FECP** deve ser registrado no **registro D761**.

Para gerar o registro do **Bloco D**, é necessário que o sistema esteja atualizado com uma data do **fonte do SPED FISCAL superior a 11/08/2025** e também é necessário executar o **UPDDISTR** com o últimodicionário de dados disponível.

Orientamos o preenchimento das informações a fim de evitar a ocorrência de erro na geração do **registro D700**.

Acesse as Informações complementares são buscadas da rotina (**MATA926 - Complementos - Comunicação e Telecomunicação**) de complemento de notas fiscais tabela **SFX** (**Complemento de comun/telecom**).

O campo **06  do registro D750**  gerado por meio do preenchimento do campo **FX\_INDPAG**.

O campo **24 do registro D700** é gerado por meio do preenchimento do campo **FX\_TIPOREC .**

Caso preencha o campo **FX\_TIPOREC** com a opção 0 - Receita própria - serviços prestados, o arquivo vai gerar o campo 24 como 0 - Faturamento Normal.  
   
Caso preencha o campo **FX\_TIPOREC** com a opção 5 - Receitas de terceiros (co-faturamento), o arquivo vai gerar o campo 24 como 2 - Cofaturamento.  
   
Caso preencha o campo **FX\_TIPOREC** com a opção 7 - Faturamento Centralizado, o arquivo vai gerar o campo 24 como 1 - Faturamento centralizado.

![Campo 24 - D700.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36697407542807)

Por padrão, todos os complementos são preenchidos manualmente.   
Caso opte por automatizar deverá ser customizado o **Ponto de entrada - MATUCOMP**.  
   
Para que o ponto de entrada **MATUCOMP** seja executado, o parâmetro **MV\_ATUCOMP** deverá estar habilitado, ou seja, preenchido com **.T.**  
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=642645988>

Ao salvar as informações na rotina de complemento ocorra o **Alerta (A926DOCOBR)** e não haja informações disponíveis para o preenchimento dos campos, é necessário seguir as orientações conforme a documentação abaixo:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/8746011684631-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Complementos-MATA926-Help-Um-ou-alguns-campos-obrigat%C3%B3rios-n%C3%A3o-foram-preenchidos>

Documentação relacionada ao **registro D700** e complemento:

[23720996 DSERFIS1-31678 DT - SPEDFISCAL - Geração dos registros D700 e Filhos - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=952384252)

[SPDFIS - Complemento dos Documentos Fiscais (Legislação SPED Fiscal) - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=702823719#SPDFISComplementodosDocumentosFiscais(Legisla%C3%A7%C3%A3oSPEDFiscal)-ClassesdeConsumo%E2%80%93MATA971)

*Link* para atualização da Rotina e aplicação do dicionário.

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049615333-Cross-Segmentos-Backoffice-Protheus-FIS-Atualiza%C3%A7%C3%A3o-do-Ambiente-Fiscal-M%C3%B3dulo-09-Livros-Fiscais>
