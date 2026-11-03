---
article_id: 360025329234
category: RH - Integração de Titulo
content_hash: 6721e6997ae44cf3eee173c2cd64a06cd397c8af87a3a4855692d157471263ce
fetched_at: '2026-06-28T22:43:36.205288+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o título de pensão automaticamente
  com dados do beneficiário como fornecedor
type: support-article
updated_at: '2025-08-01T19:07:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025329234-RH-Linha-Protheus-GPE-Como-configurar-o-t%C3%ADtulo-de-pens%C3%A3o-automaticamente-com-dados-do-benefici%C3%A1rio-como-fornecedor
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33558016101527)**Tempo aproximado para leitura: 00:04:00 min

**Dúvida**Como gerar título de pensão automaticamente com dados do beneficiário como fornecedor?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Versão 12.  
  
**Solução**  
Para configurar a geração de títulos de pensão automaticamente com os dados do beneficiário como fornecedor, realize os seguintes passos:  
  
**Passo a Passo referente ao cadastro de Beneficiários:**

1. Acesse módulo SIGAGPE
2. Acesse rotina Atualizações -> Funcionário -> Beneficiários
3. Selecione beneficiário desejado e clique em Ações Relacionadas -> Alterar
4. Identifique os campos Cod.Fornec. e Loja Fornec.
   1. Será necessário possuir um Fornecedor para cada Beneficiário para possuir o nome do beneficiário no título.
   2. O cadastro de Fornecedor pode ser feito através da própria consulta padrão presente no campo (RQ\_FORNEC) sem haver necessidade de sair da rotina de Beneficiários para fazer o cadastro.
   3. Defina o registro de Fornecedor referente ao Beneficiário e confirme.
   4. Os campos Cod.Fornec., e Loja Fornec. devem estar preenchidos.
5. Se houver mais de um beneficiário para o mesmo funcionário, repita o procedimento presente no item 4.
6. Confira os dados e confirme.
7. Repetir o procedimento a todos beneficiários desejados.

1. Acesse **Atualizações -> Funcionários -> Beneficiários  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039274034)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040114633)**

2. No campo **"Código Fornecedor",** selecione incluir e efetue o cadastro do fornecedor de acordo com as informações do beneficiário. O cadastro de Fornecedor pode ser feito através da própria consulta padrão presente no campo (RQ\_FORNEC) sem haver necessidade de sair da rotina de Beneficiários para fazer o cadastro.  
Defina o registro de Fornecedor referente ao Beneficiário e confirme.

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039274214)**

**Passo a Passo referente à geração de títulos:**

1. No módulo SIGAGPE, acesse Miscelânea -> Títulos -> Definição
2. Clique em Incluir
3. Preencha os campos Cod.Título, Descr. Título conforme desejado
4. No campo Agrupamento, escolha a opção 4 - Funcionário
5. Preencha os demais campos do cabeçalho conforme desejado
6. O valor informado no campo Cod.Fornec. e Loja Fornec. presente neste cadastro será utilizado como valor padrão para os Beneficiários que possuírem o campo RQ\_FORNEC e RQ\_LOJA em branco.
   1. Para os beneficiários com esses campos preenchidos, será utilizado o valor no cadastro de beneficiários.
7. Preencha os dados sobre Vencimento do Título conforme desejado.
8. Na área Títulos disponíveis para seleção, selecione opção Pensão Alimentícia.
9. No campo Gerar p/ Beneficiário, selecione a opção 1=Sim.
10. Confira os dados e confirme.
11. Acesse Miscelânea -> Títulos -> Geração
12. Preencha os parâmetros conforme desejar, selecionando o título que definiu para Pensão Alimentícia com geração para Beneficiário
13. Confira os dados e confirme.
14. Aguarde o processamento.
15. Acesse Miscelânea -> Títulos -> Manutenção para verificar a geração dos títulos.
16. Verifique que foram gerados títulos para cada Fornecedor presente no cadastro de Beneficiários.
    1. Se houver algum beneficiário com pensão calculada que não possui Fornecedor cadastrado, seu valor será incluído no título do fornecedor presente na Definição de Títulos.

Na definição de títulos, o usuário deve informar no campo **Agrupamento**, o conteúdo igual a **Funcionário**, o campo **Gerar p/ Beneficiário** ficará habilitado, de forma que seja permitido escolher as opções para geração dos títulos por beneficiário.

Como parte da obrigatoriedade dos campos **Cod.Fornec***.* e **Loja Fornec.**, estes deverão ser sempre preenchidos, entretanto, se o usuário desejar utilizar outro **fornecedor específico para o beneficiário**, basta cadastrar os campos **Cod.Fornec** e **Loja Fornec.**  no **cadastro de Beneficiários** que a geração irá utilizar estas informações (conforme passo 1).

***Observação:***As ações acima **somente** serão válidas para títulos de **Pensão Alimentícia** definido no padrão. Os títulos definidos por usuário não terão a mesma tratativa.

Veja que embora o campo Código do Fornecedor esteja preenchido, a rotina não considerará o fornecedor deste cadastro, buscando o fornecedor cadastrado na tabela SRQ (beneficiários)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050284013)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039276794)

4. Efetue o cálculo da folha de pagamento e verifique o cálculo da pensão:   
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040117753)  
  
5. Acesse **Miscelânea -> Títulos -> Geração** e configure os parâmetros para geração do título de pensão alimentícia:   
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040118473)  
6. O título será gerado de acordo com o cadastro de fornecedor efetuado/integrado no cadastro de beneficiários:    
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039279454)  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)  
[Documentação da implementação da funcionalidade na rotina](https://tdn.totvs.com/pages/releaseview.action?pageId=223162749)
