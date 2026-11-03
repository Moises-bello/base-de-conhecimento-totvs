---
article_id: 12072324087575
category: GPE - eSocial - Processo Trabalhista
content_hash: ecde23f60696524535e22e393f244accc3fcf800a8d54fcfcc68160412b3a14d
fetched_at: '2026-06-28T22:45:00.663855+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2501 - Como incluir tributo para geração
  do evento S-2501 no leiaute S-1.3
type: support-article
updated_at: '2025-11-18T12:09:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12072324087575-RH-Linha-Protheus-GPE-eSocial-S-2501-Como-incluir-tributo-para-gera%C3%A7%C3%A3o-do-evento-S-2501-no-leiaute-S-1-3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18062037078295) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como incluir tributos de processos trabalhistas para geração do evento S-2501 no leiaute S-1.3?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Após a inclusão das informações no evento S-2500, deve incluir o S-2501, caso necessário.  
**Acesse** a rotina TAFA552D - Atualizações > Processos Trabalhistas - Dados eSocial  
  
A primeira tela é o **Filtro**, que exibe o processo que já teve o tributo incluído através desta tela, incluir tributos para um novo caso e a possibilidade de excluir ou editar.   
  
**1-** Para **buscar um Processo** específico basta informar o número nos campos correspondentes e clicar na lupa (![](https://tdn.totvs.com/download/thumbnails/731213540/image2023-1-3_18-17-30.png?version=1&modificationDate=1672832129693&api=v2)).  
  
**2 - Se for o primeiro cadastro**, deve-se clicar no botão **+ Incluir tributo.****3 -** Caso seja necessário editar ou excluir o tributo já lançado, clique na **lixeira para excluir** e no **lápis para editar.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33104987531287)  
**Número do Processo**: utilizado o número informado no S-2500 para realizar a busca do S-2501 quando já estiver gravado;  
**Mês/Ano:** utilizados para busca do S-2501 já gravado;  
**Sequencial:** campo informado em eventos S-2501 já gravados anteriormente com número de sequencia preenchido;  
**Carregar mais resultados:** para demonstrar mais eventos S-2501 gravados  
  
Na próxima tela ao clicar em incluir tributos, é necessário informar o **número do processo** vinculado ao S-2500, **ano e mês** conforme a **data de sentença** e se necessário, informar o **número sequencial** atribuído pela empresa a cada conjunto de dados de tributos decorrentes de processo trabalhista.  
Após informar os dados anteriores, o sistema mostrará o processo vinculado ao S-2500 em **Associar trabalhadores ao processo**.  
No caso de existir outro S-2501 com mesmo numero de processo e sequencial, o sistema demonstrará os vinculos em **Trabalhadores vinculados ao mesmo processo**.  
**Atenção**, a data informada em **Mês / Ano** é a competencia em que é devida a **obrigação de pagar a parcela.**  
![chrome_Jo0LLe5eB8.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/35178125769239)  
  
Ao selecionar o processo teremos as Informações do período e base de cálculo, Informação do IRRF e Informação de retenção na fonte e dependentes:![](https://centraldeatendimento.totvs.com/hc/article_attachments/33104987534999)  
  
Aba **Informação do período e da base de cálculo dos tributos**, a data que deve ser informada no campo Referencia, deve ser **conforme informação da Competência Inicial e Competência Final** nos períodos lançados no S-2500.  
Clique em **Incluir Período**  
![smartclient_3Pkbbq5pOg.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33104987535767)  
  
Aba **Informação de IRRF** teremos:  
- Informações de valores, códigos de receita e outros  
- Dedução do rendimento tributável relativa a dependentes  
- Informação dos beneficiários da pensão alimentícia  
- Identificação dos advogados  
- Informações de processos relacionados a não retenção de tributos ou a depósitos judiciais![smartclient_9b0vblBAtS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33104987536407)Na **aba Informação de retenção na fonte e dependentes**, será possivel informar:- Data da moléstia grave atribuída pelo laudo  
- Informações de dependentes **![smartclient_niZDV6ATkB.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33104960712727)**

Para que o botão **SALVAR** fique habilitado é necessário que todos os campos obrigatórios sejam preenchidos em todas as abas exibidas. Quando um campo for obrigatório ele não exibirá a palavra (opcional). Porém, pelo leiaute do eSocial alguns campos são definidos como opcionais, porém passam a ser obrigatórios dependendo das informações digitadas em outros campos.  
  
Após **salvar a contribuição e salvar o período**, clique em **Salvar**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36290453501335)  
  
**Selecione o trabalhador** associado no processo e depois **clique em Salvar** novamente.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36290465049879)  
  
Clique em **Confirmar**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36290453509271)  
  
Esta regra pode ser visualizada através da [documentação técnica disponibilizada pelo eSocial.](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-03-2025/index.html#evtContProc)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[Artigos RH Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971467-RH-Processos-Trabalhistas)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
