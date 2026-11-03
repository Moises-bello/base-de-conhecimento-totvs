---
article_id: 15662032067863
category: TAF - eSocial - Relatório
content_hash: a16bf3695e5f997786d8b6a29f23b41973ce969683e260f9c37285588da1c920
fetched_at: '2026-06-28T22:45:19.984918+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Relatório - S-5002 - Relatório IRRF personalizado
  dentro da rotina
type: support-article
updated_at: '2026-06-17T19:13:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15662032067863-RH-Linha-Protheus-TAF-eSocial-Relat%C3%B3rio-S-5002-Relat%C3%B3rio-IRRF-personalizado-dentro-da-rotina
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15662007079319) Tempo aproximado para leitura: **00:10:00 min****Dúvida**Como gerar um relatório personalizado do totalizador S-5002 - Imposto de Renda Retido na Fonte por Trabalhador?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - TAFA422 (S-5002) - Todas as versões.

  
  
**Solução**Os relatórios personalizados podem ser criados diretamente nas rotinas do TAF.

Esta documentação traz um exemplo, para criar um relatório do totalizador S-5002 (TAFA422).

1. Acesso o TAF, entre na rotina do totalizador S-5002

Atualizações > Eventos Esocial > Totalizadores > IRRF por trabalhador

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26031149569047)

2. Para criar/montar o relatório com as informações que precisa, selecione o botão "Imprimir", na parte superior da tela.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15660827827351)

3. Será aberta a tela  “Impressão”, selecione o tipo de extensão que deseja gerar o relatório (Planilha, PDF, etc.).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31740305536279)

4. Selecione o botão “outras ações”> personalizar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15661053232151)

5. Abra as opções de Impressão, na coluna "Relatório e seção":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15661154274455)

6. Cada opção aberta, refere-se a uma tabela de negócio do TAF, que armazena determinada informação, sobre o retorno do totalizar S-5002.

7. Posicione em uma opção, e em seguida selecione o botão "células", como o exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15661320673815)

8. Após selecionar células, será possível visualizar o nome da tabela de negócio do TAF e as opções de campos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15661332126871)

9. Os campos que estiverem dentro da coluna "Células", serão apresentados no relatório que gerar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15661474579991)

10. Utilize as ferramentas entre as colunas, para inserir e retirar campos, ou desloca-los, definindo sua posição no relatório:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15661519221271)

11. Após validar e configurar todas as opções , definindo os campos que deseja no relatório, selecione o botão "Salvar".

Insira um nome para o leiaute (relatório) criado, e em seguida selecione o botão "OK".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15661659251607)

12. A tela "Salvar" será fechada, selecione o botão "ok" novamente na tela "Personalizar relatório":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15661792844055)

13. O relatório configurado, ficará disponível no campo Layout, certifique-se que o mesmo está selecionado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15661764066711)

14. Utilize o botão "Imprimir" para gerar o relatório.

15. O relatório pode ser editado, pela mesma rotina, basta mantê-lo selecionado quando for executar a manutenção.

**IMPORTANTE**

O relatório referente ao IRRF - Imposto de Renda Retido na Fonte , que será disponibilizado no Painel eSocial do Futuro (Novo Monitor) no TAF, está em desenvolvimento, com previsão para Agosto/2023 (a data pode ser alterada).

Esta documentação trás uma opção para o cliente, utilizando as ferramentas do Protheus e não realiza comparação de valores entre Folha, TAF e Governo (eSocial).
