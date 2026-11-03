---
article_id: 11983196240279
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: 91a489989726a078d770db45ed632f8f7c62c7378aa35800ead95af04982a9a4
fetched_at: '2026-06-28T22:37:49.157549+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA713 - Erro de comunicação
  - Problema ao assinar a mensagem com o certificado. Verifique se o certificado utilizado
  é válido
type: support-article
updated_at: '2026-01-07T19:24:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11983196240279-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Erro-de-comunica%C3%A7%C3%A3o-Problema-ao-assinar-a-mensagem-com-o-certificado-Verifique-se-o-certificado-utilizado-%C3%A9-v%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23869443779479)Tempo aproximado para leitura: **00:04:00 min**  
  
**Ocorrência**  
401 - Erro comunicação: Problema ao assinar a mensagem com o certificado. Verifique se o certificado utilizado é válido.

![CERTIFICADO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11982617097111)

**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA713 - Todas as versões  
  
**Causa**

O erro 401 retornado durante a validação geralmente ocorre porque o serviço necessário para a transmissão dos títulos via API não está ativado em sua conta. Recomendo que entre em contato com o banco para verificar se os serviços necessários estão devidamente ativados.

Ou acontece devido à validação dos arquivos CRT e KEY com a transmissão dos Boletos no Novo Gestor Financeiro - FINA713. O erro pode ocorrer devido ao arquivo conter o tamanho de 0KB ou 1KB, pois no padrão o tamanho ideal para os arquivos CRT e KEY, será acima de 2KB cada arquivo.

**Solução**

Entre em contato com o banco responsável pela geração dos arquivos para verificar a possível existência de inconsistências nos mesmos ou para confirmar se a conversão do certificado gerado está correta.

**Saiba mais**  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Não foi possível gerar os arquivos corretamente Erro ao extrair o Certificado de Autorização no CFGX060 Wizard de Conversão de Certificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10621741400087)  
[Itaú - Configuração Boletos - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=675571899)  
[Bradesco - Configuração Boletos - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=638386427)   
[Banco do Brasil - Configuração Boletos - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=673798283)   
[Santander - Configuração Boletos - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=653588365)
