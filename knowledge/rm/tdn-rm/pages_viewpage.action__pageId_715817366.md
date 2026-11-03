---
content_hash: 84ecced1d5c975a65d5e35e4e9145cc088ecb7d56ef50ed7c7d86317624fa1cf
fetched_at: '2026-06-29T00:11:26.109255+00:00'
page_id: '715817366'
product: rm
source: tdn-rm
title: Geral 2/2 - FOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715817366
version: 7
---

**Utiliza PPE**

Com este parâmetro marcado será habilitado o menu 'PPE' dentro do módulo Totvs Folha de Pagamento.

**Observação:** Este parâmetro está disponível somente a partir da versão 12.1.31, qualquer versão anterior a esta, deverá ser executado um script específico na base de dados que será liberado pela área de desenvolvimento conforme solicitação do usuário.

**Utiliza Combo de seção**

Com este parâmetro marcado, o campo seção no cadastro de funcionários é modificado para utilizar o combo a cada quebra de seção definido na máscara de seção.

**Exemplo**  
Mascara definida com ##.##  
Seções cadastradas:  
01.05  
01.06  
02.07  
No cadastro de funcionário será habilitado dois campos. No primeiro será carregado 01 e 02. O usuário seleciona 01. No segundo combo será carregado 05 e 06.

**Habilita Fracionamento de Jobs**  
Esse parâmetro permite fracionar a execução de processos no momento de suas gerações.  
Processos como a geração do Histórico de provisões, lançamento do grupo de eventos, lançamentos Multicoligadas e recálculo da folha.  
Será solicitado ao usuário confirmar se deseja fracionar a execução do processo e em quantas partes será dividida.  
Dessa forma o processo será fracionado em N Jobs, minimizando o tempo de execução.

[EXEMPLO DE FRACIONAMENTO DE JOBS](https://tdn.totvs.com.br/display/LRM/EXEMPLO+DE+FRACIONAMENTO+DE+JOBS)

**Utiliza cálculo de RRA**Com este parâmetro marcado, os cálculos de diferença salarial, férias, 13º Salário e Pensão Alimentícia serão lançados nos eventos de diferença de RRA para o ano anterior. Os valores encontrados nesses eventos são informados no Histórico de RRA do funcionário para que sejam considerandos na DIRF em campo específico para recebimento de RRA.

**Observações:**

Para fazer o cálculo de RRA é necessário cadastrar os eventos com os [Códigos de Cálculo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719279) específicos, conforme a necessidade.  
Caso os eventos não estejam cadastrados na base, o sistema irá emitir uma mensagem para o usuário informando que os eventos com os códigos de cálculo não foram encontrados.  
Caso seja feito uma diferença de salário no período com o mesmo ano corrente da base, será lançado os eventos de diferença padrão, mesmo com o parâmetro marcado.

Para o mês de dezembro será considerada a data de pagamento, ou seja, se o pagamento foi feito em dezembro considera como RRA e se o pagamento foi feito em janeiro considera como diferença salarial normal.

**Período Folha/Férias -** Período para lançamento da diferença de folha e/ou férias referente ao RRA e deve ser maior que 99.

**Período 13º Salário -** Período para lançamento da diferença de 13º salário referente ao RRA, deve ser maior que 99 e diferente dos outros períodos.

**Período Rescisão -** Período para lançamento da diferença de rescisão referente ao RRA, deve ser maior que 99 e diferente dos outros períodos.

Mais informações em: [Rendimentos Recebidos Acumuladamente (RRA)](https://tdn.totvs.com/pages/viewpage.action?pageId=715818269)

**Período Complemento Folha**

Período inicial deve ter o valor entre 1000 e 1999 e será gravado no mês competência do fato gerador da folha de pagamento, ou seja, será inserido novo período no mesmo mês em que o complemento da folha de pagamento foi calculado. E no mês a que se refere o complemento será gravado as verbas na pasta "Verbas geradas por diferença" na ficha financeira.

Veja mais detalhes em [Complemento da Folha de Pagamento](https://tdn.totvs.com/display/LRM/Complemento+da+Folha+de+Pagamento)
