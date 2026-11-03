---
article_id: 1500000579482
category: RH - Folha de Pagamento
content_hash: a9bf2e545fc56dcc4731ad1c6f9538e2d44a42e3bc0e8c77b2e9f20478b8290a
fetched_at: '2026-06-28T22:44:15.002329+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Importação de variáveis tabela SRK
type: support-article
updated_at: '2024-09-10T17:20:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000579482-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-SRK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26274923894039) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como efetuar importação de variáveis para a tabela SRK?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Criar um *Layout* de Importação;  
  
Acesse: Atualizações > Definições de Cálculos > ***Layout* de Importação**  
  
Exemplo: Desconto de Vales (Pode ser usado para Consignado e outros)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000620081)  
  
SRK\_FILIAL - Dados da Filial (no exemplo deixei fixo no próprio Layout)  
SRK\_MAT - Dados da matricula (informado no TXT da coluna 01 a 06)  
SRK\_PD - Dados da Verba (informado no TXT da coluna 07 a 09)  
SRK\_VALOR - Dados de Valor Principal (informado no TXT da coluna 10 a 14)  
SRK\_PARCEL - Indica o numero de Parcelas (informado no TXT da coluna 15 a 15)  
SRK\_DTVENC - Indica a Data de Vencimento do próximo desconto (informado no TXT da coluna 16 a 23)  
SRK\_NUMPAC - Numero de Parcelas (informado no TXT da coluna 24 a 25)  
SRK\_PERINI - Período Inicial a contar o debito (informado no TXT da coluna 26 a 31)  
SRK\_DTMOVI - Data da Movimentação (informado no TXT da coluna 32 a 39)  
  
Após a criação do Layout, deverá ser criado ou ajustado o **TXT**  
  
2. Criação do **TXT**;  
  
Abrir um Bloco de Notas, Clicar em **Exibir** e clicar em **Barra de Status**  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101714053)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000613022)  
  
**Observação**: Sempre que finalizar uma linha, clique em ***Enter***, para que a ultima linha do arquivo fique em branco.  
  
3. **Importar** o arquivo para o Sistema;  
  
Acesse: Miscelânea > Importação > **Importação de Variáveis**  
  
Em parâmetros selecionar o arquivo de importação:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000629081)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000629061)  
  
Selecionar o Código de *Layout* que foi criado

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000614082)  
  
Sobrepõe = SIM / NAO  
Situações = ADFT ou A\*FT

Data Referencia = Sempre a data da competência que será pago ou descontado

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099501434)

Clique em OK e OK Novamente;  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26274912826391)  
  
Clique em OK para visualizar o Log de Ocorrências;.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099502174)  
  
Importação efetuada.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101715473)  
  
Consulta por Atualizações > Lançamentos > **Valores Futuros**  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101714473)  
  
**Saiba Mais**

[RH - Linha Protheus - GPE - Importação de variáveis Coparticipação, dependentes ficam deletados na RHO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036186414-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-Coparticipa%C3%A7%C3%A3o-dependentes-ficam-deletados-na-RHO?source=search)

[RH - Linha Protheus - GPE - Importação de variáveis tabela RGB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058289233-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-RGB?source=search)

[RH - Linha Protheus - GPE - Importação de variáveis tabela RHO - Coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5743820814487-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-RHO-Coparticipa%C3%A7%C3%A3o?source=search)

[RH - Linha Protheus - GPE - É possível importar arquivo em excel com lançamentos de verbas em folha de pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409361989655-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-importar-arquivo-em-excel-com-lan%C3%A7amentos-de-verbas-em-folha-de-pagamento?source=search)

[RH - Linha Protheus - GPE - Importação de variáveis tabela RHO, não soma valores de coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000621761-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-RHO-n%C3%A3o-soma-valores-de-coparticipa%C3%A7%C3%A3o)

[RH - Linha Protheus - GPE - Importação de variáveis de coparticipação quando houver mais de 1 dependente ou agregado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038792513-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-de-coparticipa%C3%A7%C3%A3o-quando-houver-mais-de-1-dependente-ou-agregado?source=search)

[RH - Linha Protheus - GPE - GPEA210 - Ao executar a importação de variáveis ocorre a mensagem: Condição do código não está retornando valor lógico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419497227159-RH-Linha-Protheus-GPE-GPEA210-Ao-executar-a-importa%C3%A7%C3%A3o-de-vari%C3%A1veis-ocorre-a-mensagem-Condi%C3%A7%C3%A3o-do-c%C3%B3digo-n%C3%A3o-est%C3%A1-retornando-valor-l%C3%B3gico?source=search)
