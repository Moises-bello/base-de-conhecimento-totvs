---
article_id: 4407601953303
category: eSocial - Middleware
content_hash: 5bcefdc5f2bf5502d34ad3a92feb795c17454193d5a44314bb14fcbfbab14e43
fetched_at: '2026-06-28T22:47:05.614362+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Middleware - Erro: Autoridades certificadoras ausentes
  ou senha inválida'
type: support-article
updated_at: '2025-12-01T16:48:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407601953303-RH-RM-FOP-eSocial-Middleware-Erro-Autoridades-certificadoras-ausentes-ou-senha-inv%C3%A1lida
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24349821102359) Tempo aproximado para leitura: 00:02:00 min**  
  
**Ocorrência**  
Ao gerar o XML ou atualizar o certificado no parametrizador do eSocial, ocorre o seguinte erro: **Autoridades certificadoras ausentes ou senha inválida**!

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407763762967)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
O erro ocorre quando a exportação do certificado não é realizada de forma completa, ficando assim o arquivo menor que o devido. O arquivo correto deve ter tamanho maior que 7kb. Para ajuste você deve exportar novamente o certificado no navegador web. Segue orientações de exportação:

1. Clique no botão de iniciar o Windows, escreva '**Opções de Internet**' e abra a aplicação abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36695008562071)

2. Clique na aba **Conteúdo** e depois em **Certificados**. Na janela que será aberta, clique em **Importar**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407756187927)

3. No **Assistente para importação de certificados** que será aberto, avance a primeira tela. Na segunda tela, selecione o certificado que será utilizado e avance;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407762130839)

4. Na tela seguinte coloque a **senha** do certificado e marque **todas as opções de importação**. Avance até concluir o assistente;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407762170263)

5. Depois de importado ele aparecerá na lista de certificado conforme tela abaixo. Selecione o certificado e clique em **Exportar**;

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407762242967)

6. Avance ate a tela a baixo e selecione a opção **Sim, exportar a chave particular**;

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407762252695)

7. Na tela seguinte deixe marcada o parâmetro **Incluir todos os certificados no caminho de certificação, se possível**, o parâmetro **Exportar todas as propriedades estendidas** e o parâmetro **Habilitar privacidade de certificados**. Avance a tela:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407756473751)

8. Informe uma senha para o certificado e avance;

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407756533271)

9. Na tela **Arquivo a ser exportado**, informe um caminho e um nome para o arquivo e avance até concluir;  
10. Acesse o caminho indicado na etapa anterior, e verifique o tamanho do arquivo. Deve ser **maior que 7KB**.

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407762380951)

**Importante**

​​É recomendado pelas certificadoras o uso do Internet Explorer na exportação do certificado digital. Para passo a passo detalhado em outros navegadores ou sistemas operacionais, consulte a certificadora antes de qualquer ação.  
  
**Saiba mais**  
Para mais informações sobre Certificado Digital, acesse:  
     - [Middleware - Certificado Digital](https://tdn.totvs.com/display/public/LRM/Middleware+-+Certificado+Digital)
