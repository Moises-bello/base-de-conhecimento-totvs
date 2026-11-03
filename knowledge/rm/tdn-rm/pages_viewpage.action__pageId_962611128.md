---
content_hash: bc67519b9edbeddf7bcd7606c88e3c4a8809e2915b0d1595e47eed0f956858ec
fetched_at: '2026-06-29T00:12:13.975742+00:00'
page_id: '962611128'
product: rm
source: tdn-rm
title: DT - Configuração e Aplicação do Novo Cálculo do Adicional Noturno Estendido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=962611128
version: 25
---

## **01. DADOS GERAIS**

| **Produto:** | RM |
| --- | --- |
| **Linha de Produto:** | Linha RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Automação de Ponto |
| **Função:** | Parâmetros do Sindicato |
| **País:** | Brasil |
| **Requisito/Story/Issue:** | [DRHJORNRM-8204](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-8204), [DRHJORNRM-8164](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-8164) |

## **02. VERSÕES**

 A partir dos patches:

* 12.1.2506.122 e superiores

## **03. SITUAÇÃO/REQUISITO**

Permitir a definição de um intervalo de horário para que o sistema aplique o adicional noturno estendido até o fim da jornada.

## **04. SOLUÇÃO**

* Alterar o nome do parâmetro de '**Para jornadas iniciadas até XX:XX**' para "**Para jornadas iniciadas entre XX:XX até XX:XX**".
* Permitir que o usuário defina um intervalo de horário no qual o adicional noturno estendido deve ser aplicado.
* Ajustar o cálculo do adicional noturno para respeitar esse intervalo.

## **05.** **EXEMPLO DE UTILIZAÇÃO**

11Configuração

O período em que o adicional noturno estendido será aplicado deve ser configurado em: **Parametrizar Sindicato > Etapa 5 - Adicional Noturno > Considera adicional noturno até o fim da jornada > Para jornadas iniciadas entre XX:XX até XX:XX**.Esse intervalo define que jornadas iniciadas dentro desse período terão o adicional noturno estendido até o fim da jornada.

Importante

**1:** Fique atento à configuração do parâmetro do adicional noturno estendido. É fundamental ajustar a configuração conforme a sua operação, pois o adicional estendido só será aplicado se o início da jornada ocorrer dentro do período estipulado. Caso os funcionários iniciem o trabalho antes ou depois do intervalo definido, o adicional noturno estendido não será concedido.  
  
  
**2:** O horário final do intervalo do adicional noturno estendido deve estar dentro do período do adicional noturno cadastrado. Caso esteja fora desse limite, o sistema não prosseguirá e um alerta será exibido.  
  
  
  
**3:** Caso queira que o intervalo para aplicar o adicional noturno estendido seja válido durante todo o dia, ou seja, por um período contínuo de 24 horas, basta definir o parâmetro '**Para jornadas iniciadas entre 00:00 até 00:00**'. Dessa forma, qualquer jornada terá o adicional noturno estendido, desde que seja uma jornada passível de extensão.

2Cálculo

**Configurações do funcionário de exemplo:**

* **Horário do funcionário:** 22:00 - 02:00 / 03:00 - 05:00
* **Período do Adicional Noturno:** 22:00 - 05:00
* **Período do Adicional Noturno Estendido:** Para jornadas iniciadas entre 22:00 até 04:00 - **Isso significa que jornadas iniciadas dentro desse período terão o adicional noturno estendido até o fim da jornada**.

**Exemplo 1:** Jornada iniciada às 21:59, antes do intervalo definido, o sistema não deve estender o adicional noturno até o fim da jornada.  
  
  
O adicional noturno parou de ser contabilizado corretamente às 05:00.

**Exemplo 2:** Jornada iniciada às 22:00, no início do intervalo definido, o sistema deve estender o adicional noturno até o fim da jornada.

O adicional noturno foi estendido até o fim da jornada às 05:15.  
  
  
**Exemplo 3:** Jornada iniciada às 01:45, dentro do intervalo definido, o sistema deve estender o adicional noturno até o fim da jornada.

O adicional noturno foi estendido até o fim da jornada às 05:10.  
  
  
**Exemplo 4:** Jornada iniciada às 04:00, no fim do intervalo definido, o sistema deve estender o adicional noturno até o fim da jornada.

O adicional noturno foi estendido até o fim da jornada às 05:15.  
  
  
**Exemplo 5:** Jornada iniciada às 04:30, após o intervalo definido, o sistema não deve estender o adicional noturno até o fim da jornada.

O adicional noturno parou de ser contabilizado corretamente às 05:00.

## **06. ASSUNTOS RELACIONADOS**

* [Adicional Noturno](https://tdn.totvs.com/display/LRM/Adicional+Noturno)
