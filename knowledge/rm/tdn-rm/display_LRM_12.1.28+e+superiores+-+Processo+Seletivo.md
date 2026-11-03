---
content_hash: 36180a51dc743760025ebc65cc205749bb2b3f4cf5992ef35ca3b05b911dfa35
fetched_at: '2026-06-29T00:10:43.022239+00:00'
page_id: '549499256'
product: rm
source: tdn-rm
title: 12.1.28 e superiores - Processo Seletivo
type: documentation
url: https://tdn.totvs.com/display/LRM/12.1.28+e+superiores+-+Processo+Seletivo
version: 5
---

IMPORTANTE

A partir da versão 12.1.28 a instalação dos novos portais foram modificadas para que os mesmos sejam utilizados na mesma porta dos portais Corpore.Net, sendo assim, as URL's que são disponibilizadas para seus clientes devem ser modificadas.

Novo padrão de URL:

* Portal do aluno:  [http://](http://xn--local_de_instalaoporta-s4b9g/)[SERVIDOR](http://SERVIDOR/NOMEAPLICATIVO_CORPORE.NET/)[/FrameHTML/web/app/Edu/PortalEducacional/login](http://xn--local_de_instalaoporta-s4b9g/)
* Portal do Processo Seletivo: [http://](http://xn--local_de_instalaoporta-s4b9g/)[SERVIDOR](http://SERVIDOR/NOMEAPLICATIVO_CORPORE.NET/)[/FrameHTML/web/app/Edu/PortalProcessoSeletivo/#/es/informacoes](http://xn--local_de_instalaoporta-s4b9g/)

Os passos abaixo devem ser seguidos para uma utilização correta dos portais.

Depois de instalar a Biblioteca RM siga os passos abaixo para instalar o novo portal do aluno.

A instalação poderá ser completa ou personalizada.

* **Completa**: O sistema irá instalar todos os portais: Novo portal do aluno e Novo portal do processo seletivo, onde ambos serão instalados automaticamente.

* **Personalizada**: Será instalado o portal específico, isto é, o usuário irá selecionar qual Portal que deseja instalar.

Para ambas instalações, seguir o mesmo procedimento:

**1º-** A instalação inclui a estrutura do Corpore.NET (Referente ao antigo portal ) e a estrutura da FrameHTML (Referente a instalação dos Novos portais).

**2º**- Acesse o endereço: **H[ttp://LOCAL\_DE\_INSTALAÇÃO/FRAMEHTML](ttp://LOCAL_DE_INSTALA%C3%87%C3%83OPORTA)/WEB/APP/EDU/PORTALPROCESSOSELETIVO/#/ES/INFORMACOES**

Aviso

Os passos do Wizard continuam o mesmo do Portal antigo, portanto avançar como já é realizado pela instituição.

Dica

Validar de forma correta a porta e o nome do servidor caso não for utilizar localhost.

Caso a instituição deseje utilizar os novos portais como nas versões antigas, utilizando a porta 8080, acesse o link para realizar os ajustes: <https://tdn.totvs.com/x/eLmnI>

IMPORTANTE

Caso a instalação seja realizada em um diretório virtual, é necessário que a configuração do Novo Portal do Aluno em: "C:\Totvs\RM\FrameHTML\web\js\totvs-app.global.config.js " seja alterado para o nome do diretório de instalação, conforme o print abaixo.
