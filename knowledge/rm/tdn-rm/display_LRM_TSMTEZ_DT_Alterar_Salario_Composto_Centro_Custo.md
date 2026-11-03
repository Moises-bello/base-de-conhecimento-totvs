---
content_hash: f62fcb270a0635023f72ffdf1729118e1d2d1d36d350122dbdecef7fc00c2d26
fetched_at: '2026-06-29T00:06:02.608289+00:00'
page_id: '198947907'
product: rm
source: tdn-rm
title: TSMTEZ_DT_Alterar_Salario_Composto_Centro_Custo
type: documentation
url: https://tdn.totvs.com/display/LRM/TSMTEZ_DT_Alterar_Salario_Composto_Centro_Custo
version: 2
---

# ALTERAÇÃO GLOBAL DE SALÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | ``` Alteração Global de Salários ``` |
| **Função:** | ``` Atualizar salário composto por centro de custo ao realizar alteração salarial. ``` |
| ``` Situação/Requisito: ``` | ``` Quando é realizado uma alteração global de salário para funcionário que tem o salário composto distribuído por centro de custo, o sistema não está atualizando a distribuição. ``` |
| ``` Solução/Implementação: ``` | ``` Para realizar a distribuição por centro de custo do salário composto o sistema passa a verificar os seguintes itens: ```  * ```   Parâmetro 'Reprogramar salário por centro de custo' está marcado;   ``` * ```   A distribuição atual está batendo com o valor total do salário composto;   ```  ``` Para calcular quanto será distribuído para o novo valor o sistema irá considerar o percentual do valor da distribuição por centro de custo atual sobre o valor total, com isso irá calcular o novo valor. ```  ``` Exemplo: ```  ```     Salário Composto: 1500,00 ```  ``` Distribuição por cento de custo: ```  ```     Centro de Custo 01.01 - 600,00 ```  ```  Centro de Custo 01.02 - 900,00 ```  ```   ```  ``` O sistema consegue identificar que 600 é 40% e 900 é 60% do salário composto total. ```  ```   ```  ``` Se o novo salário composto for R$ 2000,00 a nova distribuição ficará: ```  ``` Centro de Custo 01.01 - 800,00 ```  ``` Centro de Custo 01.02 - 1200,00 ```     Mensagens exibidas no log:   1. Caso tenha algum registro na distribuição por centro de custo e o total da distribuição não está igual ao salário composto do evento o sistema irá exibir um aviso informando que a distribuição não será feita para o evento; 2. Ao calcular uma distribuição por centro de custo e não encontre esse centro de custo será exibido um erro impedindo a alteração de salário desse funcionário. Essa situação pode ocorrer por algum problema na base de dados, como é uma situação inesperada o sistema irá impedir a atualização;     Para notificar a modificação no produto será exibido a seguinte mensagem na rotina de Alteração Global de Salário:  *"A alteração global de salário irá redistribuir o salário composto por centro de custo conforme o percentual do valor já atribuído sobre o valor total.*  *Em caso de dúvida entre em contato com o suporte."* |
| **Chamados relacionados:** | TSMTEZ |
| **Versões/Release:** | *11.82.41* |
