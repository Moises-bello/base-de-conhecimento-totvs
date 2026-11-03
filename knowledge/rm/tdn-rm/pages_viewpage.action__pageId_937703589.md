---
content_hash: 086e2d8133ad7c2ef38a82f83335bd41364721d4710b6ad9157ccd2e1f3286ee
fetched_at: '2026-06-29T00:12:08.528336+00:00'
page_id: '937703589'
product: rm
source: tdn-rm
title: DT - S-2206 - Geração das informações relacionadas ao aprendiz
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=937703589
version: 8
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | S-2206 - Geração das informações relacionadas ao aprendiz |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11877](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11877) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2406.269
* 12.1.2410.222
* 12.1.2502.138 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Ao alterar a categoria eSocial de “103 - Aprendiz” para “101 - Empregado”, o sistema desabilita automaticamente a aba “Dados do Aprendiz” e limpa todos os campos preenchidos. Dessa forma, ao gerar o eventoS-2206 - Alteração de Contrato de Trabalho/Relação Estatutária, as **Informações Relacionadas ao Aprendiz** não são incluídas no envio.

**04. SOLUÇÃO**

Foi realizada uma tratativa no produto para garantir a geração das Informações Relacionadas ao Aprendiz mesmo em casos de alteração de categoria. Para isso, foram feitos ajustes no menu Administração de Pessoal | Funcionários | Aba Registro, de forma que, ao alterar a categoria eSocial de **"103 - Aprendiz"** para **"101 - Empregado"**, o sistema mantenha a aba **"Dados do Aprendiz"** habilitada, preservando os dados preenchidos.

O sistema continuará exibindo a aba e mantendo os dados preenchidos sempre que, no menu Administração de Pessoal | Funcionários | Históricos | Histórico da Categoria eSocial, existir um registro com o código de Categoria eSocial igual a **103**.  
Essa tratativa garante que, ao gerar o evento **S-2206 - Alteração de Contrato de Trabalho/Relação Estatutária**, as informações do grupo `<aprend>` sejam corretamente consideradas.

**Exemplo:**  
Funcionário admitido como **aprendiz** em **01/10/2023** com a Categoria eSocial preenchida com  "103 - Aprendiz**".**  
Em **01/08/2024**, o funcionário teve a alteração de categoria para **"101 - Empregado"**.  
Com a nova tratativa, mesmo após a mudança de categoria, a aba **"Dados do Aprendiz"** permanece habilitada e com as informações preenchidas, pois existe um histórico de categoria "**103 - Aprendiz"** registrado.

Assim, ao gerar o evento **S-2206**, as informações relacionadas ao aprendiz continuam sendo corretamente enviadas no grupo `<aprend>.`

Para o exemplo mencionado acima, no mês de **07/2024** foi gerado o evento **S-2206**, com data de alteração em **01/07/2024**, ainda com o funcionário na categoria eScocial "103-Aprendiz"  
Observe que o grupo `<aprend>` foi gerado corretamente, conforme demonstrado no print abaixo:

Já no mês de 04/2025, foi gerado outro evento **S-2206**, com data de alteração em **25/04/2025**, agora com o funcionário na categoria eScocial "101-Empregado".  
Observe que, nesse caso, o grupo `<aprend>` **não foi gerado corretamente**, conforme demonstrado abaixo:

## **05. DOCUMENTAÇÃO**
