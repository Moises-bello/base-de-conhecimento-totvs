---
article_id: 21862558711191
category: Entrada de dados
content_hash: 1234c14994f2edfeb1c58e1f21fcece01c1ba70bae3470792405147e08bf4691
fetched_at: '2026-06-28T22:46:30.558369+00:00'
product: rm
section_id: 1500000835061
source: central-rm
title: RH - RM - PTO - Como cadastrar terminal de coleta no Automação de Ponto
type: support-article
updated_at: '2025-10-23T20:03:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21862558711191-RH-RM-PTO-Como-cadastrar-terminal-de-coleta-no-Automa%C3%A7%C3%A3o-de-Ponto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21862528599831) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como cadastrar terminal de coleta (relógio de ponto) no Automação de Ponto?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Solução**Para registrar o terminal de coleta (relógio) no Automação de Ponto, siga as instruções abaixo:

1. Acesse o menu **Entrada de Dados | Cadastros** e selecione a opção de adicionar um novo item.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21862528603671)
2. Clique no botão novo para incluir, e vai ser aberto a tela de cadastro do terminal de coleta. Preencha o código do terminal, a descrição, se o terminal estiver em funcionamento, marque flag Terminal Ativo, salve o cadastro.

   Observação: Por padrão, o Tipo de Terminal irá vir com default o tipo Ponto.  
   E somente de preencher estes campos, este terminal já pode ser utilizado para importar as batidas que sigam o layout AFD (Arquivo de Fonte de Dados) das portarias 1510 e 671.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21862528608663)  
   Abaixo estão as informações sobre as funcionalidades de cada campo:  
     
   **Tipo REP:** Indique o tipo de REP (Registro Eletrônico de Ponto) conforme especificado na portaria 671.  
   **Localização:** Informe o local de instalação do terminal.  
   **Diferencia Natureza das Batidas:** Escolha se o terminal se refere apenas às batidas de entrada ou saída da jornada de trabalho.  
   **Natureza das Batidas:** Selecione a natureza da batida (entrada ou saída) em que as marcações serão registradas neste terminal. Esta opção estará disponível apenas se a opção "Diferencia Natureza das Batidas" estiver marcada.  
   **Seção vinculada ao Relógio**: Indique a seção à qual este terminal está alocado.  
   **Código de Fabricação:** Forneça o código de fabricação do REP, localizado no terminal.  
   Tipos de terminais:  
   **Ponto:** As batidas importadas por um terminal do tipo Ponto serão visualizadas no espelho do funcionário.

   **Refeitório:** As batidas importadas por um terminal do tipo Refeitório são consideradas como batidas de refeição e serão importadas para o anexo de refeições no cadastro do funcionário.  
     
   ***Nota***: *As opções a seguir são exclusivamente para controle de acesso e não são utilizadas para importação de batidas de ponto de funcionários ou visitantes*.  
     
   **Acesso1**: Destinado ao acesso dos funcionários ao terminal, com controle feito exclusivamente pelo RM Acesso.  
   **Acesso2:** Destinado ao acesso dos funcionários ao terminal, com controle feito exclusivamente pelo RM Acesso.  
   **Estacionamento**: Destinado ao acesso dos funcionários ao estacionamento, com controle feito exclusivamente pelo RM Acesso.

Em casos de layout customizado, se o código do terminal de coleta estiver inserido no arquivo de importação de batidas, ao realizar a importação o sistema conseguirá identificar se o funcionário pode utilizar o terminal de coleta, a natureza da batida e o tipo do terminal.

Além disso, será necessário associar um layout de relógio ao terminal para que o sistema consiga ler o arquivo (txt) no momento da importação. O layout deverá conter todas as informações que o sistema precisa para importar as batidas coletadas pelo relógio de ponto.

A utilização dos terminais de coleta está relacionada ao parâmetro 'Controla acesso de funcionários a terminais de coleta' que fica disponível nos Parametrizador Inicial do Automação de Ponto.

A importação de batidas fará as considerações do terminal de coleta somente se o layout de relógio estiver contemplando o layout.  
  
**Saiba Mais:**[TDN - Terminais de Coleta](https://tdn.totvs.com/display/LRM/Terminais+de+Coleta)[TDN- Alterações Globais de Terminais de Acesso](https://tdn.totvs.com/pages/viewpage.action?pageId=452719869)  
[PORTARIA MTP Nº 671](https://www.normaslegais.com.br/legislacao/portaria-mtp-671-2021.htm)
