---
article_id: 360036973234
category: 'Aplicativo MNTNG '
content_hash: 3e222a52bb57a84d413c5f756aa34667ef0995a143a837e0847ab2d6718a2ada
fetched_at: '2026-06-28T22:42:37.708490+00:00'
product: protheus
section_id: 360010992174
source: central-protheus
title: Manufatura - Linha Protheus - APP MNT - Implementando o Mobile MNTNG
type: support-article
updated_at: '2026-06-23T12:28:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036973234-Manufatura-Linha-Protheus-APP-MNT-Implementando-o-Mobile-MNTNG
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23033981482647)*** Tempo aproximado para leitura: **00:01:15 min**  
  
**Dúvida**  
Como configurar o *mobile* **MNTNG**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Aplicativo MNTNG - Todas as versões  
  
**Solução**  
Partindo da premissa que o ambiente **Protheus** está devidamente configurado com o módulo de **Manutenção de Ativos - SIGAMNT** ou **Gestão de Frotas - SIGAGFR**, é necessário realizar as seguintes configurações:

* **Licenças**  
  1. Verificar no License Server Virtual, se existem licenças com o código **3033** disponíveis, **caso não possua será necessário entrar em contato com o ESN da empresa para contratação**.  
  2. Solicitar um alias Mingle em [https://mingle.totvs.com.br](https://mingle.totvs.com.br/landpage/) para a utilização do **MNTNG**, ao solicitar o *alias***Mingle**, não é necessário informar **Empresa**/ **Filial**, o *alias***Mingle** deve ser **ÚNICO**para o ambiente.
* No **Protheus**:  
    
  1. [Configuração de Webservice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6977594936087-Manufatura-Linha-Protheus-APP-MNT-Configura%C3%A7%C3%A3o-WebService-Rest-Aplicativo-MNTNG?source=search)  
  2. [Configuração de campo de log](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036044933)  
  3. [Configuração de usuários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037464893)  
  4. Informar o parâmetro **MV\_NG1KEY** da seguinte forma: ALIASMINGLE;CNPJ;NOME DA EMPRESA, como por exemplo **ALIAS TESTE;99987890091000;Empresa Teste**  
  5. Incluir um [Grupos (MNTA915-SIGAMNT)](https://tdn.totvs.com/pages/viewpage.action?pageId=776518560)  
  6. Incluir [Permissões e usuários (MNTA916-SIGAMNT)](https://tdn.totvs.com/pages/viewpage.action?pageId=776519036) ao grupo  
  7. Incluir [Filtros (MNTA917-SIGAMNT)](https://tdn.totvs.com/pages/viewpage.action?pageId=776519049) ao grupo

* No **Dispositivo**:  
    
  1. [Instalação do Aplicativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003358902)
