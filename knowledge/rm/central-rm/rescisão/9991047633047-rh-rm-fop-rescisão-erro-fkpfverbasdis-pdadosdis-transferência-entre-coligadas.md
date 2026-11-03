---
article_id: 9991047633047
category: Rescisão
content_hash: 019216de2dd2bde422bdf4422c2738e43dae6a568412ddcd775c5e11e58caec6
fetched_at: '2026-06-28T22:46:54.311359+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH- RM - FOP - Rescisão:  "ERRO FKPFVERBASDIS_PDADOSDIS" transferência entre
  coligadas'
type: support-article
updated_at: '2026-05-25T14:00:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9991047633047-RH-RM-FOP-Rescis%C3%A3o-ERRO-FKPFVERBASDIS-PDADOSDIS-transfer%C3%AAncia-entre-coligadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26844083053975) Tempo aproximado para leitura: **00:02:47 min**  
  
**Ocorrência**  
Por que está aparecendo o erro ERRO FKPFVERBASDIS\_PDADOSDIS ao cadastrar transferência entre coligadas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões.  
  
**Causa**

Este erro é apresentado pois quando realizamos transferência entre coligadas, cadastros de dados do dissídio devem ser informados em ambas coligadas.   
  
**Solução**

O erro mencionado "FKPFVERBASDIS\_PDADOSDIS" na transferência de funcionário é relacionado ao cadastro de acordo coletivo, na coligada de destino não deve  haver os mesmos cadastros da coligada origem, o ajuste pode ser feito através da inclusão manual ou por meio da rotina de cópia entre coligadas.

Inclusão Manual:

1. Deverá validar em **E-Social | Acordo Coletivo/Reajuste por Lei** nas duas coligadas e caso exista algum registro divergente, ou seja, que tenha o cadastro apenas em uma coligada, deve-se realizar a inclusão do registro na coligada sem a informação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26844045901207)

2. Cadastre na coligada de destino do funcionários os mesmos acordos coletivos cadastrados na coligada de origem:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9991220377879)

:

* **Data de assinatura do acordo:** Informe a data que o acordo foi firmado e assinado;
* **Data de efeito:** Informe a data que o dissídio passará a valer;
* **Tipo do acordo:** Selecione o tipo de acordo que sua empresa adotou;
* **Competência acordada para pagamento:** Competência e ano de pagamento do dissídio;
* **Descrição:** Campo disponibilizado para acrescentar alguma observação sobre o acordo.

Rotina de Cópia entre Coligadas:

1. Para realizar o processo de forma automática sem a necessidade de inserção manual, acesse o cadastro do Dissídio.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40717197161367)
2. Clique em **Processos | Cópia de Registros entre Coligadas**.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40717165596951)
3. Na janela de "**Parâmetros da cópia**", o sistema listará todas as coligadas disponíveis na base de dados. Selecione a coligada ou as coligadas de destino para as quais deseja fazer a cópia do registro.

   **Nota**: A coligada não ficará disponível caso o usuário não tenha permissão de acesso para a mesma.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40717197161879)

   4.  Se necessário, marque a opção "Substitui registros no destino se eles já existirem". Esta opção deve ser utilizada quando o registro já existe na coligada de destino mas precisa ter os seus dados atualizados e sobrepostos pelas informações da coligada de origem. Se a opção for mantida desmarcada, o sistema preservará os dados já existentes no destino.

   5. Para concluir o Assistente de Cópia de Registros entre Coligadas e finalizar o processo, clique no botão "Executar".

**Saiba mais**

[RH - RM - FOP - Transferência entre filiais ou coligadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020186252-RH-RM-FOP-Transfer%C3%AAncia-entre-filiais-ou-coligadas)

[RH - RM - FOP - Cópia de registros entre coligadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021778232-RH-RM-FOP-C%C3%B3pia-de-registros-entre-coligadas)
