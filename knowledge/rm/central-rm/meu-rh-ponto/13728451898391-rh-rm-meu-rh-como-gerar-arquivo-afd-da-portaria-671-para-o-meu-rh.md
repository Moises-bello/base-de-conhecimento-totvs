---
article_id: 13728451898391
category: Meu RH - Ponto
content_hash: 16138ed244de28db574fefada0cc4e3a75ca018f50006815758be0a127e4d61c
fetched_at: '2026-06-28T22:47:30.292722+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Como gerar arquivo AFD da portaria 671 para o Meu RH
type: support-article
updated_at: '2025-09-17T13:10:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13728451898391-RH-RM-Meu-RH-Como-gerar-arquivo-AFD-da-portaria-671-para-o-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**  
Como gerar o arquivo AFD da portaria 671 para as batidas coletadas(geolocalização) no Meu RH.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas às versões  
  
**Solução**Permissões:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13728203154327)

Para gerar o layout AFD é necessário acessar o menu executar no ERP e localizar a tela 'AFD - Relatório Arquivo de Fonte de Dados (Portaria 671/2021)'. Exemplo:

![](https://tdn.totvs.com/download/attachments/720364372/image2022-11-3_8-10-44.png?version=1&modificationDate=1667500180367&api=v2)

![](https://tdn.totvs.com/download/attachments/720364372/image2022-11-9_8-41-56.png?version=1&modificationDate=1667994163383&api=v2)

Nesta tela será necessário definir o período do ponto, as datas de início e fim, quebra de seção, seleção de funcionários (opcional) e o perfil (opcional).

![](https://tdn.totvs.com/download/attachments/720364372/image2022-11-9_8-42-33.png?version=1&modificationDate=1667994200113&api=v2)

Para seguir no processo de geração é necessário confirmar a mensagem acima, que contem as orientações de preenchimento dos acordos sindicais (2 - Acordos sindicais).

![](https://tdn.totvs.com/download/attachments/720364372/image2022-11-10_11-25-36.png?version=1&modificationDate=1668090384387&api=v2)

![](https://tdn.totvs.com/download/attachments/720364372/image2022-11-10_11-25-56.png?version=1&modificationDate=1668090403757&api=v2)

Caso algum funcionário não possua batidas serão apresentados alguns alertas para cada chapa:

![](https://tdn.totvs.com/download/attachments/720364372/image2022-11-10_11-26-22.png?version=1&modificationDate=1668090430323&api=v2)

![](https://tdn.totvs.com/download/attachments/720364372/image2022-11-10_11-26-41.png?version=1&modificationDate=1668090449153&api=v2)

É importante observar também as seguintes orientações:

* Somente será possível utilizar o processo através do menu executar;
* Necessário liberar as permissões (3- Liberações e permissões)
* Não será permitido inserir uma data de início anterior à data de 01 de novembro de 2021 que corresponde a data de inicio da portaria;
* Se o período inserido for diferente das datas de início e fim, as datas serão consideradas para a geração;
* Será gerado um arquivo texto por sindicato, desde que o sindicato possua funcionários que tenham batidas realizadas no Meu RH;
* As batidas consideradas devem possuir um registro na tabela APORTARIA373 e na tabela ABATFUN desde que possuam o campo IDAPORTARIA373 preenchido;
* Para gerar o arquivo para o período selecionado é importante que os dados estejam nas tabelas de produção, caso esteja no arquivo morto deverá executar o processo para transferir os dados para a produção ([Transferir dados para a tabela de produção](https://tdn.totvs.com/pages/viewpage.action?pageId=185731949));
* O arquivo terá uma nomenclatura padrão estipulado pela portaria e será complementado no final com o código do sindicato. Exemplo:

         AFD11111111111111REP\_A\_0002  - Sigla AFD + CNPJ da coligada (11111111111111) + REP\_A\_ + Código do sindicato (0002)

* Para cada sindicato é necessário preencher o código do processo do acordo sindical (2 - Acordos sindicais) , caso não seja definido este código será gerado um valor default estipulado pela portaria (99999999999999999);
* Caso já exista o arquivo na pasta selecionada ele será sobrescrito;
* A assinatura digital ainda não será gerada no layout pois está em processo de definição pelo jurídico;

## **ACORDOS SINDICAIS**

Esta tela tem por finalidade cadastrar, editar e excluir informações de acordos sindicais bem como seu período de vigência. Estas informações serão utilizadas no relatório de AFD.   
Não é permitido cadastrar acordos que contenham interseção com outro acordo cadastrado, ou seja, cadastrar um acordo com data de vigência que já possua outro acordo vigente cadastrado.

Para acessar a tela e realizar o cadastro acesse no módulo de automação de ponto: 'Configurações >>Parametrizador >> 08.02 - Sindicato > Seleção do sindicato > Acordos Sindicais' ou através do menu de funcionários: 'Funcionário >> Seleção do Funcionário >> Processos >> Parametrizar Sindicato';

![Imagem](https://media.discordapp.net/attachments/888497976983568434/1037814463803441162/unknown.png?width=873&height=630)

![Imagem](https://media.discordapp.net/attachments/888497976983568434/1037815173500637234/unknown.png)

(1) - Código acordo sindical

* Número do processo originado pelo acordo sindical;
* Preenchimento obrigatório;
* Permite informar somente números;
* Deve conter 17 caracteres.

(2) - Data de início

* Data de início de vigência do acordo;
* Preenchimento obrigatório;
* Deve ser menor que a data de fim.

(3) - Data fim

* Data de término de vigência do acordo;
* Preenchimento obrigatório;
* Deve ser maior que data de inicio.

Para mais informações sobre a portaria 671 no Meu RH acesse: [Portaria 671/2021 Meu RH](https://tdn.totvs.com/pages/viewpage.action?pageId=708884746)
