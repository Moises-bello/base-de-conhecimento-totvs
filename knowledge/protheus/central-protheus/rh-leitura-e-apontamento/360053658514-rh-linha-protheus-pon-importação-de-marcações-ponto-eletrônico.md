---
article_id: 360053658514
category: RH - Leitura e Apontamento
content_hash: f8602daebe32845f26194718cf05f2385f48105988edf72d07fd027bdfb3f586
fetched_at: '2026-06-28T22:44:45.958226+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Importação de marcações Ponto Eletrônico
type: support-article
updated_at: '2025-07-09T15:17:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053658514-RH-Linha-Protheus-PON-Importa%C3%A7%C3%A3o-de-marca%C3%A7%C3%B5es-Ponto-Eletr%C3%B4nico
---

**Dúvida**  
Como realizar a leitura das marcações gravadas no arquivo texto do Relógio de ponto?**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução  
1-** Verifique se o cadastro de **Período de Apontamento** está aberto corretamente. A data dos dados geradas pelo relógio de marcações devem estar dentre o período em aberto (Atualizações -> Cadastros Ponto -> Períodos Apontamento).

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091910373/mceclip9.png)

**2 -** Verificar o número do **PIS** no **Cadastro de Funcionários** e localizar o mesmo no arquivo ponto (TXT).  
Quando for formato **AFD**, o crachá não importa mais e sim o **PIS**, então é interessante sempre tentar confirmar se o PIS dos funcionários do **AFD** constam mesmo cadastrados no Cadastro de Funcionários do Protheus, na filial onde está sendo solicitada a leitura.  
  
Os clientes que tem muitos relógios em diversas filiais tem o hábito de pegar **AFD** de uma e ler em outra, onde não tem ninguém alocado, por conta da alta demanda. Dessa forma, não serão informados dados gravados.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091909293/mceclip0.png)

**3 -** No **Cadastro de Relógio** o campo campo **CÓDIGO** deve ter 3 dígitos  
O Campo **REP** preenchido se for o novo formato **AFD**, se não for, devem deixar sempre em branco  
O campo **CONTROLE** deverá ser preenchido com **P**O campo **Tipo Arquivo** de ser igual **T**O campo **Nome do Arquivo** deverá conter a extensão **.TXT**

No modelo **AFD**, não precisa configurar as demais abas, pois o modelo tem layout pré-definido.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089766694/mceclip1.png)

**4 -** Avaliar necessidade de realizar **Troca de****turno**  
Se for a primeira leitura verificar se o Funcionário possui **Troca de Turno** (Atualizações > Cad Func > Troca de Turno). Para que o sistema consiga montar o calendário deve existir pelo menos uma troca de turno com data de inicio anterior a data da leitura.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089766834/mceclip2.png)

**5 -** Efetuar leitura do período, deixando a pergunta **Ler a Partir do?** nos parâmetros de leitura e apontamento com a opção **CADASTRO DE RELÓGIOS**.  
Acesse a rotina para realizar  **LEITURA E APONTAMENTO** em Miscelâneas > Cálculo > Leitura/apontamento. Confira o preenchimento dos parâmetros.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091909853/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089766954/mceclip4.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091909913/mceclip5.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091909993/mceclip6.png)

Após a leitura o sistema ira emitir o Log de ocorrências especificando os detalhes da leitura\apontamento e possíveis erros.   
Em atualizações > lançamentos > marcações podemos visualizar as marcações geradas pelo relógio.

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089768994/mceclip10.png)

**Para auxiliar nos passos confira documentações:**

[MP - PON - Como alterar dia inicial e final do período de apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013375112-MP-PON-Como-alterar-dia-inicial-e-final-do-per%C3%ADodo-de-apontamento?source=search)

[MP - PON - Como efetuar o cadastro do Relógio Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004209412-MP-PON-Como-efetuar-o-cadastro-do-Rel%C3%B3gio-Ponto?source=search)

[MP - PON - Como funciona a troca de turno dos funcionários?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671-MP-PON-Como-funciona-a-troca-de-turno-dos-funcion%C3%A1rios-?source=search)

[MP - PON - Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-MP-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o-?source=search)

[MP - PON - Como gerar os Apontamentos no SIGAPON?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052257014-MP-PON-Como-gerar-os-Apontamentos-no-SIGAPON-?source=search)

[MP - PON - Processo de leitura e apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003918712-MP-PON-Processo-de-leitura-e-apontamento?source=search)
