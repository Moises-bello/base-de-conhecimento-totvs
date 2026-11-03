---
article_id: 360024984152
category: Originação de Grãos (OG)
content_hash: f85beb0cc6bf682fbd902c2ff8389daebb5b428d48ee30f30bd26f25db5d35a4
fetched_at: '2026-06-28T22:45:39.629723+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Impressão Word Contratos
type: support-article
updated_at: '2025-06-23T15:50:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024984152-Agro-Linha-Protheus-AGR-Impress%C3%A3o-Word-Contratos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20402586880023)**Tempo aproximado para leitura: **00:02:35 min****Dúvida**Ao tentar imprimir um arquivo de Word no **Contrato de Compra - OGA280**, a impressão do arquivo não ocorre corretamente, e em vez de serem impressas as informações do contrato, são impressas apenas as variáveis utilizadas para chamar as informações. Como proceder?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - A partir da versão 12  
  
**Solução**Para que sejam impressas as informações do contrato em vez das variáveis, o passo a passo abaixo deve ser seguido:  
1. Acessar a rotina de Contrato, Ações Relacionadas **Imprimir Word**. Na opção **Parâmetros** informar o local do arquivo **.DOT** usado como modelo, e em seguida, informar o local onde o arquivo será salvo.

![Screenshot_1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023756151)

2. Depois das informações acima serem concluídas, clicar em **OK**.  
3. Após, clicar na opção **Impr. Documento**.  
4. O arquivo de Word será aberto assim:

![Screenshot_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023756371)

5. Copie a variável que será substituída. No caso do exemplo, a variável substituída será a: **AGR\_CPFVENDEDOR**.  
6. Após copiar a variável, selecione a linha toda de variáveis, conforme abaixo:

![Screenshot_6.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023718332)

7. Depois, com a linha das variáveis selecionada, na aba **Inserir**, selecione a opção **Campo**.

![Screenshot_4.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023756951)

8. Na tela que será aberta, selecione a opção **DocVariable**, e no campo **Novo Nome**, cole o conteúdo anteriormente copiado: **AGR\_CPFVENDEDOR**.

![Screenshot_7.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023718792)

9. Ao clicar em Ok, o conteúdo será substituído.

![Screenshot_8.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023718872)

**Importante**Esse procedimento deve ser feito linha a linha para todas as variáveis, e o arquivo deve ser salvo e armazenado como modelo, pois nas outras vezes em que for utilizado, entenderá as alterações e o procedimento não necessitará ser realizado novamente.  
O procedimento descrito acima pode ser utilizado tanto na rotina **de Contrato de Compra - OGA280**, como na rotina de **Contrato de Venda - OGA290**.
