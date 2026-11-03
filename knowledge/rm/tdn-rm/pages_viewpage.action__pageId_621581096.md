---
content_hash: fa3918faf0c99f9cbb4552089c26f6ba04b916a3f1495e2d748adeae49a2b0ea
fetched_at: '2026-06-29T00:11:03.377715+00:00'
page_id: '621581096'
product: rm
source: tdn-rm
title: Atualização Versão 12 ou Superiores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=621581096
version: 2
---

Todos os aplicativos necessários para a conversão da biblioteca RM 12 estão disponíveis na própria instalação da Biblioteca .MSI, tanto os módulos em Delphi quanto o Conversor, que na verdade mudou de nome e passou a ser o RM Atualizador, segue abaixo os links dos documentos necessários para atualização:   
  
[Documento da Portabilidade.](http://tdn.totvs.com/display/public/LRM/PORTABILIDADE)  
[Manual do Atualizador.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000994448-RM-BD-D%C3%BAvida-Como-converter-atualizar-a-Base-de-Dados-RM-)  
[Cuidados para Conversão.](http://tdn.totvs.com/pages/releaseview.action?pageId=61933314)

Favor proceder com a seguinte configuração:

1. Desinstale a Biblioteca RM atual, seguindo os passos do artigo [Como desinstalar a Biblioteca RM](https://totvssuporte.zendesk.com/knowledge/articles/115015991067/pt-br?brand_id=1509248);  
   **Importante**  
   Observar os requisitos necessários para uso;  
   Caso tenha customizações nos arquivos config, realize backup dos mesmos. Os arquivos são localizados no diretório RM.Net, conforme exemplo no print abaixo:  
     
   O arquivo de configuração do RM Portal está localizado no diretório Corpore.Net, conforme exemplo abaixo:
2. Realize a instalação partindo do zero, utilizando o instalador .MSI. Exemplo: BIBLIOTECARM-12.1.29.MSI, lembrando de observar os requisitos necessários para uso;  
   [Instalação Biblioteca RM 12.1.](http://tdn.totvs.com/pages/viewpage.action?pageId=267784174)

Siga os requisitos abaixo:

* Framework 4.7.2 ou superiores;
* Firewall desabilitado;
* Antivírus desabilitado;
* UAC Controle de acesso de usuários desabilitado;

**Importante**  
Qualquer dúvida referente à conversão e validação do seu banco, entre em contato com a equipe de suporte do Banco de dados.  
Telefone: (11) 4003-0015 opção 2-2-3-8
