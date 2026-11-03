---
article_id: 1500004469422
category: RH - Benefícios
content_hash: 3941daaecaff9bcdac3798335a7eb008800bec9e85a5a23c37ee620466ba19dd
fetched_at: '2026-06-28T22:44:03.526089+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro e Cálculo de Vale Combustível
type: support-article
updated_at: '2026-06-24T20:08:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004469422-RH-Linha-Protheus-GPE-Cadastro-e-C%C3%A1lculo-de-Vale-Combust%C3%ADvel
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21239524235287) Tempo aproximado para leitura: 00:05:00 min****Dúvida**Como parametrizar e calcular Vale Combustível?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Siga os passos abaixo para cadastrar e calcular o benefício de Vale Combustível:  **1.** Cadastro do Roteiro BEN  
Acessar em **Atualizações> Definições de Cálculo> Período**s e inclua o roteiro **BEN - Outros Benefícios.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005472682)**

**2.** Cadastro das Verbas  
Acessar em **Atualizações> Definições de Cálculo> Verbas**, e crie três verbas, sendo uma de Provento, uma de Desconto e outra de Base Provento. Todas as verbas **não** devem ter Identificador de Cálculo.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005571761)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005473002)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005571881)

**3.** Inclusão do benefício na S011  
Acessar **Atualizações> Definições de Cálculo> Manutenção de Tabelas**, localize a tabela **S011**, clique em Outras Ações e posteriormente em Alterar. Insira uma linha, informe o código e descrição ao benefício como Vale Combustível.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005571441)

**4.** Cadastro do Vale combustível na rotina de Definições de Benefícios   
Acessar **Atualizações> Benefícios:> Outros Benefícios> Definição de Benefícios.** Selecione o tipo de Benefício Vale Combustível e clique em Manutenção para cadastrar o benefício;

Abaixo, um exemplo de **possível** preenchimento. Será pago ao funcionário um valor fixo de R$ 150,00 mensalmente, e deste valor será descontado 10% do Funcionário e o restante, ficará como parte Empresa.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005473582)  
  
Preenchimento dos campos:  
**- Código:** Defina um código de identificação do benefício.  
**- Descrição:** Atribua uma descrição ao benefício.  
**- Salário Até ou Quantidade de Salário Mínimo:** Informe o valor de salário limite para o recebimento do benefício, escolhendo entre salário até ou quantidade de salário mínimo.  
**- Tipo Referência:** Escolha entre três tipos de cálculo para o benefício: valor fixo, percentual salário base ou percentual salário mínimo.  
**- Referência:** Informe o valor de referência que será utilizado no cálculo  
**- % Pagamento Funcionário:** Informe o percentual de pagamento do funcionário (Com base no campo Referência)  
**- Tipo de Desconto:** Selecione entre as opções de Percentuais (Benefício, Salário Base e Salário Mínimo)  
**- Desconto do Funcionário:** Defina o percentual de desconto do funcionário   
**- Cód Verba:** Informe a verba de pagamento (se houver)  
**- Verba Desc.:** Informe a verba de desconto funcionário (se houver)  
**- Verba Empres:** Informe a verba parte empresa (se houver)  
**- Proporc:** Informe se o valor do benefício será calculado baseado nos dias trabalhados no mês  
**- Pag. Falta:** Informe se haverá o pagamento do benefício quando houver faltas  
  
  
**5.** Inclusão do Vale combustível para o funcionário  
Acessar em **Atualizações> Benefícios> Outros Benefícios> Manutenção** para amarrar o Vale Combustível ao funcionário. Posicione na matrícula desejada, clique em **Manutenção** e preencha os campos principais campos:  
  
**- Tipo Benefício:** Preencha este campo com o tipo de benefício de Vale Combustível  
**- Código Benefício:** Insira o código do benefício que o funcionário terá direito  
Após preencher o campo Código Benefício, o sistema preenche automaticamente os campos referente as verbas (que foram cadastradas na rotina de Definição de Benefícios)  
  
Em seguida preencha o restante dos campos:  
**- DT. Ini. Pag:** Informe a data para inicio do cálculo**- Dt. Fim. Pag:** Informe a data de encerramento (campo não obrigatório)  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005473822)

**6**. Cálculo do benefício  
Acessar em **Atualizações> Benefícios> Outros Benefícios> Cálculo**, clique em Parâmetros e informe:  
**- Processo:** Informe qual processo deseja calcular  
**- Roteiro:** Escolha o roteiro de Outros Benefícios: **BEN**  
Os campos Período e Nr Pagamento serão preenchidos automaticamente e, caso queira, preencha o filtro. Clique em **Calcular**. No final do processo um **LOG** será gerado com as informações do cálculo processado.  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005573361)![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005573401)  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005474162)  
  
  
**7.** Relatório para conferência ou visualização do cálculo individualmente  
Para imprimir o relatório, acessar em **Atualizações> Benefícios> Outros Benefícios> Relatório Cálculo,** clique em **Outras Ações/Parâmetros** e informe: **Processo,** **Período do cálculo** e **Tipo do Benefício** que deseja imprimir, os demais parâmetros podem ser configurados conforme necessidade.  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005474302)  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005474322)  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005474602)  
  
Caso queira consultar o cálculo individualmente, acesse **Atualizações/ Benefícios/ Outros Benefícios/ Manutenção**, selecione o funcionário desejado e clique **Outras Ações/ Visualização do Cálculo.**![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005574321)

**8.** Integração do roteiro BEN à folha de pagamento  
Após todo este processo de cálculo e conferência, o Roteiro BEN deve ser integrado ao Roteiro FOL, para que os valores sejam efetivamente pagos, para isso, acessar em **Atualizações> Benefícios> Outros Benefícios> Integração com Folha** e integre o Roteiro BEN a folha de pagamento. Após este procedimento, o sistema levará para a tabela **RGB** em **Atualizações> Lançamentos> Por Funcionário.  
![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005475382)**  
  
**9.** Fechamento do Roteiro  
Após todas as conferências do cálculo na folha, no final do período é necessário realizar o fechamento do roteiro BEN. Para realizar o procedimento, acessar em **Atualizações> Benefícios> Outros Benefícios> Fechamento,** selecione o Roteiro BEN e clique em Confirmar.   
 **OBS:** Para que seja feito o fechamento corretamente, é necessário ter o roteiro BEN cadastrado para o próximo período.

**10.** Histórico de Cálculo  
A rotina de Histórico do Cálculo, possibilita visualizar todos os benefícios já calculados para determinado funcionário. Para executar a rotina, acessar em **Atualizações> Benefícios> Outros Benefícios> Histórico Cálculo,** selecione o funcionário desejado e clique em visualizar.  
![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005575341)  
  
**Filtros:** Caso desejar, filtre a visualização por tipo de benefício e/ou período. Caso queira visualizar o histórico completo deixe os campos em branco e clique em OK. Ao final, a tela de histórico exibirá os dados dos benefícios pagos ao funcionário escolhido.  
  
![](https://tdn.totvs.com/download/attachments/353281227/image2018-4-16_9-58-7.png?version=1&modificationDate=1523883880000&api=v2)  
  
![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005575501)  
  
  
  
**Saiba Mais**[DT Verificação de faltas no roteiro BEN](https://tdn.totvs.com/pages/viewpage.action?pageId=729236877)  
[RH - Linha Protheus - GPE - Relatório de Outros Benefícios em planilha (GPER065)](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj2h9rUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MzM3NzAxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUmVsYXQlQzMlQjNyaW8tZGUtT3V0cm9zLUJlbmVmJUMzJUFEY2lvcy1lbS1wbGFuaWxoYS1HUEVSMDY1BjsIVDoOc2VhcmNoX2lkSSIpMDc1NzcwNzItMjNjYy00ZWNiLWE4NWUtZDVjZGY4ZGE4ODc4BjsIRjoJcmFua2kMOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIQcm90ZWlybyBCRU4GOwhUOhJyZXN1bHRzX2NvdW50aQL%2FAg%3D%3D--7a28cf617c5137909782f7a3fef6eeae298c9bf7)  
[RH - Linha Protheus - GPE - Arquivo de benefícios para o Roteiro BEN - Outros Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXeanT%2Bws6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBomh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzEzMTc2MjE1Nzk2MTE5LVJILUxpbmhhLVByb3RoZXVzLUdQRS1BcnF1aXZvLWRlLWJlbmVmJUMzJUFEY2lvcy1wYXJhLW8tUm90ZWlyby1CRU4tT3V0cm9zLUJlbmVmJUMzJUFEY2lvcwY7CFQ6DnNlYXJjaF9pZEkiKTA3NTc3MDcyLTIzY2MtNGVjYi1hODVlLWQ1Y2RmOGRhODg3OAY7CEY6CXJhbmtpCDoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiEHJvdGVpcm8gQkVOBjsIVDoScmVzdWx0c19jb3VudGkC%2FwI%3D--6017d4743cf3027b80eb7cee267109c15732e12e)  
[RH - Linha Protheus - GPE - Como suspender o cálculo de beneficio para um funcionário por tempo indeterminado](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwji9wrVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBt2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NjU1MTM5NC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby1zdXNwZW5kZXItby1jJUMzJUExbGN1bG8tZGUtYmVuZWZpY2lvLXBhcmEtdW0tZnVuY2lvbiVDMyVBMXJpby1wb3ItdGVtcG8taW5kZXRlcm1pbmFkbwY7CFQ6DnNlYXJjaF9pZEkiKTA3NTc3MDcyLTIzY2MtNGVjYi1hODVlLWQ1Y2RmOGRhODg3OAY7CEY6CXJhbmtpDjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiEHJvdGVpcm8gQkVOBjsIVDoScmVzdWx0c19jb3VudGkC%2FwI%3D--f5642a891c984f2bf7abe7e199c7be2b80d17b06)  
[RH - Linha Protheus - GPE - É possível realizar o cálculo de 1 benefício quando o funcionário tem 2 cadastrados no roteiro BEN](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj1ZcDUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIB12h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1MTY2NDM3My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtJUMzJTg5LXBvc3MlQzMlQUR2ZWwtcmVhbGl6YXItby1jJUMzJUExbGN1bG8tZGUtMS1iZW5lZiVDMyVBRGNpby1xdWFuZG8tby1mdW5jaW9uJUMzJUExcmlvLXRlbS0yLWNhZGFzdHJhZG9zLW5vLXJvdGVpcm8tQkVOBjsIVDoOc2VhcmNoX2lkSSIpMDc1NzcwNzItMjNjYy00ZWNiLWE4NWUtZDVjZGY4ZGE4ODc4BjsIRjoJcmFua2kJOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIQcm90ZWlybyBCRU4GOwhUOhJyZXN1bHRzX2NvdW50aQL%2FAg%3D%3D--8d60ee83ab1ff7178d25609a8129bf2ed4a2ef2e)
