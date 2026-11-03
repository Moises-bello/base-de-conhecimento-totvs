---
article_id: 360058289233
category: RH - Lançamentos
content_hash: e857d105559fb613243384bb2e6bc7494886c2effac1474a499a61cc7922f6c1
fetched_at: '2026-06-28T22:43:31.286570+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Importação de variáveis tabela RGB
type: support-article
updated_at: '2025-04-17T18:49:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058289233-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-RGB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como efetuar importação de variáveis para a tabela RGB?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Criar um Layout de Importação;  
  
Acesse: Atualizações > Definições de Cálculos > **Layout de Importação**  
  
Exemplo: Desconto Farmácia (Pode ser usado para pagamento de Hora Extra, Gratificação entre Outros)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095749014/mceclip0.png)  
  
RGB\_FILIAL - Dados da Filial (no exemplo deixei fixo no próprio Layout)  
RGB\_MAT - Dados da matricula (no exemplo estou informando que está no TXT da coluna 01 a 06)  
RGB\_PD - Dados da Verba (no exemplo deixei fixo no próprio Layout)  
RGB\_VALOR - Dados de Valor (no exemplo estou informando que está no TXT da coluna 08 a 15)  
RGB\_CC - Opcional a utilização, mas pode-se deixar amarrado com a formula: SRA->RA\_CC  
  
Após a criação do Layout, deverá ser criado ou ajustado o TXT  
  
2. Criação do TXT;  
  
Abrir um Bloco de Notas, Clicar em **Exibir** e clicar em **Barra de Status**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098052093/mceclip1.png)  
  
Observação: Sempre que finalizar uma linha, clique em ***Enter***, para que a ultima linha do arquivo fique em branco.  
  
3. **Importar** o arquivo para o Sistema;  
  
Acesse: Miscelânea > Importação > **Importação de Variáveis**  
  
Em parâmetros selecionar o arquivo de importação:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098065513/mceclip4.png)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095756874/mceclip3.png)

Selecionar o Código de Layout que foi criado

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098069693/mceclip5.png)  
  
Sobrepõe = SIM / NAO  
Situações = ADFT ou A\*FT

Data Referencia = Sempre a data da competência que será pago ou descontado

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095773554/mceclip6.png)

Clique em OK. Preencha os demais parâmetros:  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098070253/mceclip7.png)  
  
Clique em OK e OK Novamente;  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095773954/mceclip8.png)  
  
Clique em OK para visualizar o Log de Ocorrências;.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095774134/mceclip9.png)  
  
Importação efetuada.  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098070633/mceclip10.png)

**Observação:** Por padrão o sistema realiza a importação de variáveis e preenche o campo RGB\_TIPO2 (Origem) com G. Esse campo especificamente, está chumbado no fonte GPEA210 com tipo G - Gerado,  independente da configuração do Layout criado.   
Só será preenchido com I se a verba que está sendo realizada a importação constar na RGB.   
  
**Saiba Mais**

[RH - Linha Protheus - GPE - O que conferir quando há inconsistência na importação do txt de coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049408533-RH-Linha-Protheus-GPE-O-que-conferir-quando-h%C3%A1-inconsist%C3%AAncia-na-importa%C3%A7%C3%A3o-do-txt-de-coparticipa%C3%A7%C3%A3o?source=search)

[RH - Linha Protheus - GPE - Importação de variáveis Coparticipação, dependentes ficam deletados na RHO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036186414-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-Coparticipa%C3%A7%C3%A3o-dependentes-ficam-deletados-na-RHO?source=search)

[RH - Linha Protheus - GPE - Importação de variáveis tabela SRK](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000579482-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-SRK?source=search)

[RH - Linha Protheus - GPE - Como realizar a importação de variáveis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018541331-RH-Linha-Protheus-GPE-Como-realizar-a-importa%C3%A7%C3%A3o-de-vari%C3%A1veis?source=search)

[RH - Linha Protheus - GPE - Importação de variáveis tabela RHO - Coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5743820814487-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-RHO-Coparticipa%C3%A7%C3%A3o?source=search)
