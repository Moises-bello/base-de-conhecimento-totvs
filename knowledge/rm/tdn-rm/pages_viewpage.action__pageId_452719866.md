---
content_hash: fd463f4d1b1b74ade98ac7319716ad6e9913547e91d31a269c5e9d6b52adbf6c
fetched_at: '2026-06-29T00:10:10.531669+00:00'
page_id: '452719866'
product: rm
source: tdn-rm
title: Histórico de Assistência à Saúde
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719866
version: 7
---

Atendendo a **Instrução Normativa RFB nº 1.033, de 14 de maio de 2010**, será armazenado o valor descontado de Assistência Médica e/ou Odontológica do funcionário e de seus dependentes como histórico de assistência a saúde.  
   
***"Artigo 10,*** *§ 3º:  No caso dos rendimentos de que trata o inciso II do § 1º, se o empregado for beneficiário de plano privado de assistência à saúde, na modalidade coletivo empresarial, contratado pela fonte pagadora, deverão ser informados os totais anuais descontados em folha de pagamento, correspondente à participação do empregado, discriminando as parcelas correspondentes ao beneficiário titular e as de cada dependente."*  
   
Neste histórico constam os beneficiários que participam do desconto do Plano de Assistência à Saúde e seu preenchimento pode ser efetuado automaticamente pelo sistema ou através de importação ou inclusão manual feita pelo usuário.  
Para a informação ser enviada automaticamente para o histórico, deverá ser adaptada a fórmula que atualmente é utilizada para o desconto da assistência á saúde, informando a variável de fórmula: SALVAVALDEP( , ).

Veja também o TDN[Fórmulas / Funções – S - SALVAVALDEP](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719340)   
   
Para os casos que o Histórico de Assistência à Saúde necessite de ser importado para o cadastro do funcionário, deverá ser utilizado o módulo de Importação de Dados do Folha de Pagamento.  
   
**Observações:**

1. Quando na geração da DIRF/Informe de Rendimentos, em algum mês, não for encontrado registro no anexo 'Histórico Assistência à Saúde' e existir evento no envelope do funcionário referente ao desconto de assistência à saúde, o sistema assumirá o valor do evento para o beneficiário Funcionário.
2. Somente serão visualizados os eventos sem código de cálculo ou com o código de cálculo 14-Assistência Médica.
3. Os campos 'Ano Referência', 'Mês Referência' e 'Período Referência' são referentes ao mês em que foi processada a diferença e somente são visíveis na tela quando o 'Tipo de Movimento' é de 'Diferença'.
4. Caso o campo 'Somente com incidência' esteja marcado, serão visíveis apenas os dependentes que possuem o campo '**Assistência Médica**' ou/e  '**Assistência Odontológica**' marcado na aba 'Incidência' do cadastro do dependente e o funcionário.

**Atenção**  
1. Quando houver restituição do valor da assistência à saúde, para que o sistema alimente a tabela automaticamente, o usuário deverá criar uma fórmula informando o valor negativo e informar no evento.   
**Exemplo:** Fórmula retornar -100  
Caso o usuário deseje alimentar a tabela manualmente, também deverá informar o valor negativo.

---

Funcionários
