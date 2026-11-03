---
article_id: 360050319614
category: Gestão de Transportes (TMS)
content_hash: 32e6347a3a0cc2cb8c2d4cafb6b6adb6046f2077fc9f6c4bf200651dfd517cb4
fetched_at: '2026-06-28T22:45:27.318287+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Cadastros básicos para geração de contrato
  carreteiro
type: support-article
updated_at: '2022-07-19T12:41:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050319614-Log%C3%ADstica-Linha-Protheus-TMS-Cadastros-b%C3%A1sicos-para-gera%C3%A7%C3%A3o-de-contrato-carreteiro
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:10 min****Dúvida**Quais os cadastros principais relacionados para geração do contrato de carreteiro no **SIGATMS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Os cadastros principais relacionados para geração do contrato de carreteiro no **SIGATMS – Gestão de Transportes**são:

1. **Natureza:** Acesse **SIGATMS: Atualizações / Cadastros / Natureza - FINA010**  
   Devem ser cadastradas naturezas para geração de título de pedágio, pessoa física, pessoa jurídica e a natureza que será utilizada quando o título de carreteiro for gerado em alguma filial de débito.  
   Campos que afetam o processo com pessoa física:
   * **Calcula IRRF - ED\_CALCIRF**
   * **Calcula INSS - ED\_CALCINS**
   * **Porc INSS** **- ED\_PORCINS**
   * **Base INSS - ED\_BASEINS**
   * **Calc SEST - ED\_CALCSES**
   * **Base SEST - ED\_BASESES**
   * **Porc SEST - ED\_PERCSES**
   * **IRRF Carret**. **-** **ED\_IRRFCAR**
   * **Base IR Car**. **-** **ED\_BASEIRC**
   * **INSS Carret**. **- ED\_INSSCAR**
2. **Despesas:** Acesse **SIGATMS: Atualizações / Transporte / Despesas - TMSA060**  
   Podem ser associadas as informações contábeis.  
   Devem ser criadas despesas para o contrato de carreteiro e uma despesa para geração de título de pedágio. Estas despesas são utilizadas para a apuração dos custos de transportes das viagens.
3. **Cadastro de Fornecedores:** Acesse **SIGATMS – Atualizações / Cadastros / Fornecedores - MATA020**  
   Se o campo **Natureza - A2\_NATUREZ**, na aba**Adm/Fin.**, estiver com o conteúdo em branco, o Sistema adota a natureza informada no parâmetro **MV\_NATCTC - Natureza do contrato de carreteiro**.  
   O fornecedor deve possuir condição de pagamento informada no campo **Cond Pagto. - A2\_COND**, na aba **Adm/Fin.**  
   Para a pessoa física é necessário informar se calcula **INSS - Instituto Nacional do Seguro Social**, no campo **Calc. INSS - A2\_RECINSS** na aba **Fiscais** e na aba **TMS** informar os campos **Recolhe SEST - A2\_RECSEST**, **Dependentes - A2\_NUMDEP**, **Cód. INSS - A2\_CODINSS**. O campo **RNTRC - A2\_RNTRC** deve ser informado para os dois tipos de fornecedores.  
   **Fornecedor Genérico:** Quando todos os fornecedores da transportadora forem utilizar o mesmo tipo de contrato de fornecedor, é possível utilizar somente este fornecedor no cadastro.
4. **Veículo:** Acesse **SIGATMS: Atualizações / Transporte / Veículos - OMSA060**  
   É necessário associar o cadastro do veículo ao fornecedor, por meio do campo **Proprietário - DA3\_CODFOR**.  
   O campo **Frota - DA3\_FROVEI**, deve ser definido como **Terceiro** ou **Agregado**.
5. **Motorista:** Acesse **SIGATMS: Atualizações / Transporte / Motoristas - OMSA040**  
   É necessário cadastrar um motorista.  
   O campo **Tp. Motorista - DA4\_TIPMOT**, deve estar definido como **Terceiro** ou **Agregado**.  
   O motorista deve estar vinculado a um Fornecedor.
6. **Tabela IRRF:** Acesse **SIGACFG: Ambiente / Cadastros / Tabela IRRF**  
   Devem ser informados os dados da tabela progressiva.
7. **Tabelas genéricas:** Acesse **SIGACFG: Ambiente / Cadastros / Tabelas**  
   Por meio da tabela **05** do **Configurador**, crie o tipo de título para o título de carreteiro por filial e o tipo de título para pedágio

**Saiba mais**Para mais informações acesse as documentações:[Logística - Linha Protheus - TMS - Principais parâmetros Contrato Carreteiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050187034-MP-TMS-Principais-par%C3%A2metros-Contrato-Carreteiro)  
[Logística - Linha Protheus - TMS - Contrato Carreteiro com o parâmetro MV\_LIBCTC habilitado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057773133-MP-TMS-Contrato-Carreteiro-com-o-par%C3%A2metro-MV-LIBCTC-habilitado)
