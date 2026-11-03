---
article_id: 1500007987582
category: RH - Transferência
content_hash: 0590f6c8443cbf17065b0668ceeeb27850cd874da129712aa45f96ed48c77887
fetched_at: '2026-06-28T22:43:23.275705+00:00'
product: protheus
section_id: 360010781974
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao fazer transferência de funcionários ocorre
  a mensagem: Não foi possível abrir o arquivo da Empresa Destino'
type: support-article
updated_at: '2025-07-24T14:11:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007987582-RH-Linha-Protheus-GPE-Ao-fazer-transfer%C3%AAncia-de-funcion%C3%A1rios-ocorre-a-mensagem-N%C3%A3o-foi-poss%C3%ADvel-abrir-o-arquivo-da-Empresa-Destino
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15937609448599) Tempo aproximado para leitura: **00:01:00**  
**Ocorrência**Ao fazer transferência de funcionários ocorre a mensagem: **Não foi possível abrir o arquivo da Empresa Destino**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011749561)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Causa**Esta mensagem indica que a tabela mencionada **não existe na base de dados da empresa destino**

**Solução**A SRO mostrada na imagem é **apenas um exemplo**, o procedimento de solução **aplica-se a qualquer tabela.**  
  
É possível fazer uma consulta através da Consulta Genérica - **Consultas/ Cadastros/ Genéricos**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011482582)  
  
1. Busque a tabela que consta na mensagem e clique em **ok,** o Sistema emitirá alerta que não há dados a serem apresentados.  
2. Clique em fechar e o Sistema abrirá a consulta vazia.   
3. Após isso, confirme no configurador se a tabela SRO da empresa em questão foi criada.

Caso a mensagem continue a ser demonstrada, crie a tabela na empresa Destino:  
  
1. Acesse o SIGACFG da empresa destino com *login* de Administrador  
2. Acesse o Base de Dados **(Base de dados/ Dicionário/ Base de Dados)**  
3. Clique na opção de inclusão de tabela, no **ícone** com "**+**"  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011756681)  
  
4. Inclua as informações da tabela que deve ser criada, incluindo seu compartilhamento. No **exemplo** colocamos a tabela SRO

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011487782)  
  
  
Caso seja uma empresa nova, é possível que o Sistema **notifique a ausência de mais tabelas**, sendo necessário criá-las acessando a rotina ou via configurador como no anexo.  
  
Além destas opções também temos a possibilidade de um **D****e/Para** da estrutura e dos índices da empresa já existente, mas este processo deve ser acompanhado por um Consultor Totvs, caso não tenham conhecimento de como proceder.

**Saiba Mais:**

[RH - Linha Protheus - GPE - É possível bloquear a transferência de funcionário desligado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9291158422167-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-bloquear-a-transfer%C3%AAncia-de-funcion%C3%A1rio-desligado)  
[RH - Linha Protheus - GPE - Como cancelar ou desfazer transferências de funcionários?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025324694-RH-Linha-Protheus-GPE-Como-cancelar-ou-desfazer-transfer%C3%AAncias-de-funcion%C3%A1rios-)  
[RH - Linha Protheus - GPE - Movimentação de Tabelas em Transferência entre Empresas/Filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057237614-RH-Linha-Protheus-GPE-Movimenta%C3%A7%C3%A3o-de-Tabelas-em-Transfer%C3%AAncia-entre-Empresas-Filiais)  
[RH - Linha Protheus - GPE - Modo de compartilhamento correto para efetivação de transferência de funcionários entre empresas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060368253-RH-Linha-Protheus-GPE-Modo-de-compartilhamento-correto-para-efetiva%C3%A7%C3%A3o-de-transfer%C3%AAncia-de-funcion%C3%A1rios-entre-empresas)  
[RH - Linha Protheus - GPE - Ao transferir o funcionário de volta para sua filial origem, apresenta a mensagem - Já existe Funcionário com a Matricula Digitada. Informe nova Matrícula](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054851754-RH-Linha-Protheus-GPE-Ao-transferir-o-funcion%C3%A1rio-de-volta-para-sua-filial-origem-apresenta-a-mensagem-J%C3%A1-existe-Funcion%C3%A1rio-com-a-Matricula-Digitada-Informe-nova-Matr%C3%ADcula)
