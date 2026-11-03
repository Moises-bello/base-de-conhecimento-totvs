---
content_hash: 3422fbb6102296d17b3868a5dbcfb031728d43ba46fc6345cc6fa2caf192bf43
fetched_at: '2026-06-29T00:10:59.808680+00:00'
page_id: '616234472'
product: rm
source: tdn-rm
title: Histórico Padrão do Movimento - Regime de Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=616234472
version: 24
---

---

No processo de [Geração do Movimento - NFe](https://tdn.totvs.com/pages/viewpage.action?pageId=425458928), pode ser utilizado um texto padrão no histórico de movimentos gerados via [TOTVS Educacional](https://tdn.totvs.com/display/LRM/Educacional). Este histórico pode ser visualizado nos Itens de Movimento do **TOTVS Gestão de Estoque, Compras e Vendas**.

O texto padrão pode contar com algumas variáveis disponibilizadas, estas variáveis têm como objetivo retornar informações específicas sobre o contrato do aluno.

**Variáveis disponibilizadas**:

* **[SRV.C]**- Código do Serviço
* **[SRV.D]**- Nome do Serviço
* **[ALU.C]**- RA do Aluno
* **[ALU.D]**- Nome do Aluno (Caso o Nome Social esteja preenchido, a tag será preenchida com essa informação. Essa regra foi descontinuada a partir dos patches **12.1.2310.199, 12.1.2402.139, 12.1.2406**, pois foi criado uma variável específica para o Nome Social do Aluno)
* **[ALU.S]** - Nome Social do Aluno. Variável disponível a partir dos patches **12.1.2310.199, 12.1.2402.139, 12.1.2406**
* **[CUR.C]**- Código do Curso
* **[CUR.D]**- Nome do Curso
* **[BOL.CX]** - Código da Bolsa
* **[BOL.DX]** - Nome da Bolsa
* **[BOL.VX]** - Valor da Bolsa
* **[PRL.C]** - Período Letivo
* **[CNT.C]** - Código do Contrato do Aluno.
* **[DCC.V]** - Desconto Condicional (Soma dos descontos condicionais do contrato). Variável disponível a partir dos patches **12.1.2402.205, 12.1.2406.134, 12.1.2410**
* **[DIC.V]**- Desconto Incondicional (Soma dos descontos incondicionais do contrato). Variável disponível a partir dos patches **12.1.2402.205, 12.1.2406.134, 12.1.2410**

Para criação do texto padrão este deve ser configurado nos parâmetros do TOTVS Educacional em **Parâmetros | Educacional | Integração | Fiscal | Histórico**

As variáveis Número de Parcela, Cota e Data de Vencimento do Lançamento não serão disponibilizadas, pois não tem vinculo com o Regime de Competência.  
Essas variáveis são de informações financeiras da parcela e só terão efeito na geração de movimento por Regime de Caixa.

* **[PAR.C]**- Número da Parcela
* **[COT.C]**- Número da Cota
* **[LAN.DV]** - Data de Vencimento do Lançamento
Tags [BOL.CX] - [BOL.DX] - [BOL.VX]

A letra 'X' das variáveis de Bolsa serve para indicar qual Bolsa será utilizada.  
Vamos supor que no contrato do aluno existam 2 bolsas associadas. Para que as duas bolsas sejam referenciadas no complemento do histórico, inclua a variável duas vezes e substitua o 'X' número de ordem da bolsa.

**Exemplo:**   
Bolsas associadas no contrato do aluno: **'FIES'** e **'Aproveitamento'**Para que o movimento leve o código, nome e valor das duas Bolsas, inclua no complemento uma variável para cada Bolsa e indique o número correspondente.

A ordem da Bolsa irá respeitar o código da Bolsa.   
As duas Bolsas associadas são:  
- Bolsa 'FIES' de código 5 com valor de 20,00  
- Bolsa 'Aproveitamento' de código 10 com valor de 30,00

Desta forma, no complemento do histórico onde o 'X' foi substituído por 1, serão apresentados os dados referentes à Bolsa 'FIES'. E onde o 'X' foi substituído por 2, serão apresentados os dados referentes à Bolsa 'Aproveitamento', assim:  
[BOL.C1] = [BOL.D1] = [BOL.V1] | [BOL.C2] = [BOL.D2] = [BOL.V2]   
5 = FIES = 20,00 | 10 = Aproveitamento= 30,00
