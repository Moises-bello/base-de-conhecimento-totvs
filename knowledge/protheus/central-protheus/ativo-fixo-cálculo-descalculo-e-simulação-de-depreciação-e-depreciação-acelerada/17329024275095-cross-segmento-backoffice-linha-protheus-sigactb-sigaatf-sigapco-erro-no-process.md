---
article_id: 17329024275095
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 89f31293d906140cbc7f7d78199bbeaa52746e32bfee7f318c29a17ca6f4aaf2
fetched_at: '2026-06-28T22:41:43.311249+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - SIGAATF - SIGAPCO -
  Erro no processo de instalação de Procedure
type: support-article
updated_at: '2025-07-03T14:37:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17329024275095-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-SIGAATF-SIGAPCO-Erro-no-processo-de-instala%C3%A7%C3%A3o-de-Procedure
---

**Ocorrência:**

Erros no processo de instalação de procedure como por exemplo:

Erro ao instalar a procedure [ATFXXX\_11\_XX] - Error : 24344 - ORA-24344: success with compilation error ( From tDBServer::ROP\_SQLEXEC )

**Ambiente:**Cross Segmento - TOTVS Backoffice Linha Protheus - Ativo Fixo -  Contábil - PCO  
  
**Causa:**

Geralmente erros de instalação de procedures ocorrem devidos a desatualização, erros no código fonte, ou erros no ambiente.  
  
**Solução:**Para solucionar essa ocorrência, realize os seguintes passos:

- Realizar Backup do RPO  
- Aplique as atualizações abaixo referente a procedure do módulo que ocorre o erro, em um **ambiente de homologação**

**Links:**  
**[Pacotes de Atualização - Ativo Fixo + Dicionário + Procedure](https://tdn.totvs.com/pages/releaseview.action?pageId=382557083)**

**[Pacotes de Atualização - Contábil+ Dicionário + Procedure](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)**

**[Pacotes de Atualização - PCO + Dicionário + Procedure](https://tdn.totvs.com/pages/releaseview.action?pageId=421375078)**

Atualize o gestor de procedures :

<https://tdn.totvs.com/pages/releaseview.action?pageId=532651679>

E Diretamente no servidor realiza o processo abaixo em modo exclusivo:1º Reinicie o serviço.

1º Desinstale as procedures existente em seu ambiente.  
2º Verifique se o sistema desinstalou do configurador.  
3º Verifique se o sistema [desinstalou do Banco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019534772-MP-SIGACTB-Saldos-n%C3%A3o-est%C3%A3o-sendo-atualizados-de-forma-online-?source=search) antes de instalar novamente.  
4º Instale as procedures .  
5º Reinicie o serviço.

- Se o procedimento acima não corrigir, solicite ao DBA da empresa que realiza a consulta abaixo:

Executar a seguinte consulta para obter os erros de compilação específicos da procedure:

- Verificar qual procedure esta apresentando erro, como exemplo utilizamos a ATFXXX\_11\_XX

- Onde ATFXXX\_11 faz referência ao nome da procedure e \_XX é o número do grupo de empresa.

Segue querys a serem realizadas, pelo **DBA**  
  
**--Oracle:**  
  
SELECT \*  
FROM user\_errors  
WHERE name = 'ATFXXX\_11\_XX';  
  
Esta consulta irá fornecer detalhes sobre os erros de compilação encontrados na  
procedure.  
  
  
**--SQL**  
  
SELECT \*  
FROM sys.messages  
WHERE language\_id = 1033 -- ID do idioma inglês  
AND text LIKE '%ATFXXX\_11\_XX%'  
AND severity > 10  
AND is\_event\_logged = 0;  
  
//language\_id = 1033

* 1033: Inglês (padrão)
* 1046: Português
* 1031: Alemão
* 1034: Espanhol
* 1036: Francês
* 1040: Italiano

**--Postgres**   
  
SELECT \*  
FROM pg\_catalog.pg\_proc p  
WHERE p.proname = 'ATFXXX\_11\_XX';

Após realizada a query colher os resultados e encaminha para o suporte para análise.

**Saiba Mais:**  
**[Stored Procedures - Novo gerenciador de pacotes](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes)**
