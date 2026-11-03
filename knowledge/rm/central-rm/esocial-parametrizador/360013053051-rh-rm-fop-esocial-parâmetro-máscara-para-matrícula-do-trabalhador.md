---
article_id: 360013053051
category: eSocial - Parametrizador
content_hash: 314dfd5dbde664d1e2ddf2d2a18e3de0fdfc0f779f0575a86d48eaf80f9321c1
fetched_at: '2026-06-28T22:47:06.347276+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: ' RH - RM - FOP - eSocial - Parâmetro Máscara para Matrícula do Trabalhador'
type: support-article
updated_at: '2024-10-30T13:29:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013053051--RH-RM-FOP-eSocial-Par%C3%A2metro-M%C3%A1scara-para-Matr%C3%ADcula-do-Trabalhador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23003220067351)Tempo aproximado para leitura: **00:03:30 min**

**Dúvida**Quais são as funcionalidades dos parâmetros do campo **Máscara para Matrícula do Trabalhador**?**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**O conjunto de configurações do campo **Máscara para Matrícula do Trabalhador** foram criadas para que o usuário defina como será o formato da máscara da matrícula do funcionário que preencherá o campo **Matrícula eSocial** automaticamente no cadastro do funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23003220081047)

A máscara é definida da junção dos caracteres dos 3 campos abaixo:

* **Prefixo**: é opcional e seu tamanho mínimo é 1. Por *default* este campo vem desabilitado e com valor 0. Para habilitar é necessário marcar a opção **utilizar prefixo**. Marcando esta opção, o campo **Prefixo** referente ao código do prefixo fica habilitado para edição. Somente é permitido preencher este campo com o código com o mesmo tamanho da quantidade de caracteres informada. Este campo pode ser preenchido com alfanumérico.
* **Coligada**: O campo recebe o tamanho mínimo 4, sendo 3 referente ao tamanho mínimo da coligada e um caractere recebe a Letra C. Caso a base tenha alguma coligada de código com tamanho maior que 3, este campo receberá como mínimo este valor. Exemplo**:** Na base existe uma determinada coligada com o código 9999, então o campo por default irá receber o valor 5 e não pode ser menor. Neste caso o campo será de tamanho 5, pois também terá o caractere C.
* **Sequencial**: O campo recebe o tamanho mínimo 7, sendo que um caractere é referente a Letra S. Exemplo: a máscara com o mínimo de caracteres seria C999S999999.

O usuário poderá aumentar a quantidade de caracteres nos três campos, limitando a soma dos três em 30 caracteres. Os valores mínimos carregados por default não podem ser diminuídos.

Caso o usuário faça a seleção do parâmetro **Gerar matrícula automaticamente na admissão de funcionário**, ao admitir um funcionário será gerada matrícula para eSocial automaticamente.  **Importante**Após fazer a configuração e/ou um Cadastro de Funcionário, onde foi inserido uma **Matrícula eSocial** no cadastro do Funcionário, caso o usuário deseje alterar a **Máscara para Matrícula do Trabalhador**, o sistema permite, porém exibe uma mensagem que pode causar duplicidade de Matrículas já geradas.

A configuração de **Máscara para Matrícula do Trabalhador** deve ser feita por Coligada.
