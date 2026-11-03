---
article_id: 360050629314
category: Comércio Exterior - Easy Import Control - Siscomex
content_hash: 5da0b1f470081e415bb8448162cd32166590560427fd2a4bbcc304e7cdb44a18
fetched_at: '2026-06-28T22:39:45.264896+00:00'
product: protheus
section_id: 1500001538441
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Check List para
  problemas de integração Siscomex Web
type: support-article
updated_at: '2021-10-28T12:30:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050629314-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Check-List-para-problemas-de-integra%C3%A7%C3%A3o-Siscomex-Web
---

**Dúvida**O que verificar para problemas de integração com o Siscomex Web?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**O ambiente deve estar:    
1° - Com as atualizações do módulo disponibilizada no [pacote acumulado do comex .](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047332793)2° - Integrador java “tr-sw-web-solution-siscomexweb.jar” encontra-se na pasta SmartClient ( este é disponibilizado no pacote acumulado e deve estar atualizado);

Verificações de teste a ser realizado:   
1° - O cliente consegue utilizar o certificado para logar no site do Siscomex Web Importação  
manualmente via browse (Internet Explores, Firefox e Chrome, por exemplo).  
2° - Acessando processos manualmente no site do Siscomex Web, se é possível realizar a  
operação que esta tentando executar pelo sistema.  
3° - Avaliar configurações de proxy por usuário (Atualizações / Int. Siscomex Web / Configurações). Deve ser informado o diretório local para transmissão dos arquivos e diretório do programa "JAVA.EXE" (<https://tdn.totvs.com/pages/releaseview.action?pageId=235335670> ), conforme exemplo :   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079016693/mceclip0.png)  
Observação: Pode ser informado as configurações do Proxy, caso tenha bloqueio de rede.   
  
4° - Configurações de proxy informados pelo administrador de rede (MV\_EIC0053,  
MV\_EIC0054, MV\_EIC0055, MV\_EIC0056).  
5° - Permissão de leitura e gravação nas pastas \protheus\_data\comex, %Temp% e diretório  
informado pelo usuário em (Atualizações / Int. Siscomex Web / Configurações).  
6° - Certificado digital válido para acesso ao Portal Siscomex Web Importação. (É  
permitido apenas um certificado por nome de usuário. Certificados duplicados geram erro no  
integrador).  
- Acessar certmgr.msc  
- Acessar Certificados > Pessoal > Certificados  
  
Persistindo o incidente após verificações no ticket de atendimento deve ser encaminhado:   
- Inspetor de objetos para análise da data dos fontes da rotina;  
- Envio dos pacotes de envio e retorno .zip para análise. (Arquivo de envio e retorno do processo. (Localizar arquivos em  
\protheus\_data\comex\siscomexweb\enviados e \protheus\_data\comex\siscomexweb\recebidos).  
- Evidência do procedimento realizado.
