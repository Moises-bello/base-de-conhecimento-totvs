---
content_hash: 67146c74db0b6bb6b14da66dc3243089ebaf13c7b735051b7d45efdf1dc04815
fetched_at: '2026-06-29T00:09:27.306916+00:00'
page_id: '423938497'
product: rm
source: tdn-rm
title: Requisitos relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938497
version: 3
---

A partir da versão 11.8x com as Demonstrações Contábeis e na 12.1.x onde vários dos relatórios oficiais do sistema de Gestão Contábil foram migrados, adotamos novas tecnologias e ferramentas visando agregar novos recursos para a gestão contábil das empresas com a emissão de relatórios mais robustos, multi-lotes, flexíveis e com novas parametrizações. Estes novos relatórios bem como a ferramenta de Demonstrações Contábeis têm como objetivo flexibilizar a gestão empresarial, dar suporte as tomadas de decisão e promover soluções contábeis ágeis e de rápida adaptação as necessidades e características individuais de cada empresa. Toda a tecnologia adotada visa disponibilizar robustez e flexibilidade, mas em contrapartida, temos limitações técnicas que obrigam adequações nos ambientes de instalação do ERP. Estas adequações para geração dos relatórios são:

Em linhas gerais, a solução e a tecnologia adotada para lidar com as características de volume de informações e flexibilidade exigidos nos relatórios da contabilidade OBRIGA a existência de um DRIVE de impressora para dar suporte à geração dos relatórios.

**Em ambiente local (Não usa 3 camadas):**

* Necessita de uma impressora instalada (Não precisa ser uma impressora física pode ser uma impressora virtual do próprio Windows por exemplo).  
  **Em um ambiente 3 Camadas:** - O ambiente precisa ter obrigatoriamente uma impressora instalada no servidor de JOB (aplicação). OBS: Não precisa ser uma impressora física pode ser uma impressora virtual.
* Instalado uma impressora no Client, as informações da impressora serão repassadas para o Server para impressão (isso não desobriga a instalação do drive de impressora do lado Server).
* Quando não existir uma impressora instalada no lado Client será utilizado o Drive da impressora server associado a uma configuração padrão repassada pelo próprio relatório a ser gerado.
